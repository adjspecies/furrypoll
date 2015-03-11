from flask import (
    Flask,
    flash,
    g,
    session,
    redirect,
    render_template,
    request,
)
from flask.ext.mongoengine import MongoEngine

import datetime
import os
import random


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'furrypoll_2015'}
app.config["SECRET_KEY"] = os.urandom(12)
app.config["DEBUG"] = False
app.config['SURVEY_ACTIVE'] = False

db = MongoEngine(app)

# Older python compat - db has to be defined first.
import models
import questions


@app.before_request
def before_request():
    """Pre-request checks

    If the survey is not active, do not allow any paths except /
    """
    if 'static' in request.path:
        return
    if not app.config['SURVEY_ACTIVE'] and request.path != u'/':
        flash('The survey is not currently active.')
        return redirect('/')


@app.route('/')
def front():
    """Render the front page"""
    return render_template('front.html', survey_active=app.config['SURVEY_ACTIVE'])


@app.route('/survey/start/', methods=['GET', 'POST'])
def surveyStart():
    """Begin a survey

    This view creates a response object if none exists and provides the user
    with some additional information about the survey.  Additionally, bot
    checks are made with a honeypot and a simple math question.
    """
    # If it's a POST request, we need to check for bots.
    if request.method == 'POST':
        if (int(request.form.get('result', '-100')) == session.get('add_a', 0)
                + session.get('add_b', 0)) \
                and request.form.get('hp_field', '') == '':
            return redirect('/survey/overview/')
        else:
            flash('''Please ensure that you have answered the simple question
            below to start the survey!''')

    # Create a new response object if none exists.
    if session.get('response_id') is not None:
        survey = models.Response.objects.get(id=session['response_id'])
    else:
        survey = models.Response()
        survey.metadata = models.ResponseMetadata(
            client_ip=request.remote_addr,
            client_ua=str(request.user_agent)
        )
        start_tp = models.Touchpoint(
                touchpoint_type=0
        )
        survey.metadata.touchpoints.append(start_tp)
        survey.save()
        session['response_id'] = str(survey.id)
        if len(models.Response.objects.filter(metadata__client_ip=request.remote_addr)) > 1:
            flash('''It appears that someone has already completed the furry
            survey from this computer or IP address.  If this is a public
            computer, a household with multiple people sharing one IP address,
            or you believe that you have not completed this survey, please feel
            free to continue; otherwise, please <a href="/survey/cancel">cancel
            the survey</a> if you have already completed it.''')
            survey.metadata.touchpoints.append(models.Touchpoint(touchpoint_type=-6))

    # Prepare bot checks.
    session['add_a'] = add_a = random.randint(1, 10)
    session['add_b'] = add_b = random.randint(1, 10)
    return render_template('start.html',
                           survey_id=str(survey.id), 
                           add_a=add_a, 
                           add_b=add_b)


@app.route('/touch/question/<int:question_id>')
def surveyQuestion(question_id):
    """Mark a question answered

    This AJAX view marks a question as answered with a touchpoint, which is
    used to judge how quickly the respondent answered each question; spam
    responses generally take place far too quickly.
    """
    if session.get('response_id') is None:
        return '{"error":"No session id"}'
    tp = models.Touchpoint(
        touchpoint_type=question_id
    )
    survey = models.Response.objects.get(id=session['response_id'])
    survey.metadata.touchpoints.append(tp)
    survey.save()
    return '{"error":null}'


@app.route('/survey/overview/', methods=['GET', 'POST'])
def surveyOverview():
    """The Overview section of the survey"""
    # Check if we have a response.
    if session.get('response_id') is None:
        return redirect('/')

    survey = models.Response.objects.get(id=session['response_id'])
    if request.method == 'POST':
        # Add a page touchpoint.
        tp = models.Touchpoint(
            touchpoint_type=-1
        )
        survey.metadata.touchpoints.append(tp)

        # Cancel if requested.
        if request.form.get('cancel') is not None:
            survey.save()
            return redirect('/survey/cancel/')

        # Save answers if provided.
        survey.overview = models.Overview()
        _save_answers(request.form, 'overview', survey)
        survey.save()

        # Complete the survey if requested.
        if request.form.get('complete', None) is not None:
            return redirect('/survey/complete')

        # Otherwise, continue on to the next page.
        return redirect('/survey/psychographic/')
    else:
        # Check if we've already completed the Overview.
        if -1 in [tp.touchpoint_type for tp in survey.metadata.touchpoints]:
            flash("Looks like you've already completed the overview...")
            return redirect('/survey/psychographic/')
        return render_template('overview.html', questions=questions)


@app.route('/survey/psychographic/', methods=['GET', 'POST'])
def surveyPsychographic():
    """The Psychographic Battery section of the survey"""
    # Check if we have a response.
    if session.get('response_id') is None:
        return redirect('/')

    survey = models.Response.objects.get(id=session['response_id'])
    if request.method == 'POST':
        # Add a page touchpoint.
        tp = models.Touchpoint(
            touchpoint_type=-2
        )
        survey.metadata.touchpoints.append(tp)

        # Cancel if requested.
        if request.form.get('cancel', None) is not None:
            survey.save()
            return redirect('/survey/cancel/')

        # Save answers if provided.
        survey.psychographic_battery = models.PsychographicBattery()
        _save_answers(request.form, 'psychographic_battery', survey)
        survey.save()

        # Complete the survey if requested.
        if request.form.get('complete', None) is not None:
            return redirect('/survey/complete')

        # Otherwise, continue on to the next page.
        return redirect('/survey/sexuality/')
    else:
        # Check if we've already completed the battery.
        if -2 in [tp.touchpoint_type for tp in survey.metadata.touchpoints]:
            flash("Looks like you've already completed the psychographic battery...")
            return redirect('/survey/sexuality/')
        return render_template('psychographic.html')


@app.route('/survey/sexuality/', methods=['GET', 'POST'])
def surveySexuality():
    """The Sexuality section of the survey"""
    # Check if we have a response.
    if session.get('response_id') is None:
        return redirect('/')

    survey = models.Response.objects.get(id=session['response_id'])
    if request.method == 'POST':
        # Add a page touchpoint.
        tp = models.Touchpoint(
            touchpoint_type=-3
        )
        survey.metadata.touchpoints.append(tp)

        # Cancel if requested.
        if request.form.get('cancel', None) is not None:
            survey.save()
            return redirect('/survey/cancel/')

        # Save answers if provided.
        survey.sexuality = models.Sexuality()
        _save_answers(request.form, 'sexuality', survey)
        survey.save()

        # Complete the survey.
        return redirect('/survey/complete/')
    else:
        # Check if we've already completed the sexuality section.
        if -3 in [tp.touchpoint_type for tp in survey.metadata.touchpoints]:
            flash("Looks like you've already completed the sexuality section...")
            return redirect('/survey/complete/')
        return render_template('sexuality.html')


@app.route('/survey/complete/', methods=['GET', 'POST'])
def surveyComplete():
    """Mark a survey as complete"""
    if session.get('response_id') is not None:
        survey = models.Response.objects.get(id=session['response_id'])
        if -4 not in [tp.touchpoint_type for tp in survey.metadata.touchpoints]:
            # Add a complete touchpoint.
            flash("Survey complete! Thank you!")
            tp = models.Touchpoint(
                touchpoint_type=-4
            )
            survey.metadata.touchpoints.append(tp)
            survey.save()
        else:
            flash("Survey is already marked as complete!")
        session['response_id'] = None
    return render_template('complete.html')


@app.route('/survey/cancel/', methods=['GET', 'POST'])
def surveyCancel():
    """Mark a survey as canceled"""
    if session.get('response_id') is None:
        return redirect('/')
    survey = models.Response.objects.get(id=session['response_id'])
    # Add a cancel touchpoint.
    tp = models.Touchpoint(
        touchpoint_type=-5
    )
    survey.metadata.touchpoints.append(tp)
    survey.save()
    flash("Survey canceled.  Thank you for your time!")
    session['response_id'] = None
    return render_template('cancel.html')


def _save_answers(form, section, survey):
    """Save question answers.

    Given a form, the section which is to be saved, and a survey response
    object, save the questions from the form in the survey response.
    """
    for key in form.keys():
        value = form.get(key, '')

        # Skip blank answers.
        if value == '':
            continue

        # Skip values from button clicks
        if key in ['submit', 'complete', 'cancel']:
            continue

        # Skip other text fields, which will be fetched manually.
        if key.endswith('_other'):
            continue

        if key in questions.question_options:
            # If it's in a list of question options, save a PSR.
            psr_lists = ['race', 'occupation']
            if key in psr_lists:
                values = form.getlist(key)
                for value in values:
                    survey.__getattribute__(section).__getattribute__(key).append(
                        _psr_from_value(form, key, value))
            else:
                survey.__getattribute__(section).__setattr__(
                    key,
                    _psr_from_value(form, key, value))
        else:
            # If it has an indicator type, utilize the proper save method.
            indicator = key[:3]
            indicated_types = {
                'gic': _save_gender_identity_coordinates,
                'npo': _save_number_per_option,
                'spo': _save_string_per_option,
                'lpo': _save_list_per_option,
                'lst': _save_list_item,
                'chr': _save_character,
                'psr': _save_raw_psr,
            }
            if indicator in indicated_types:
                indicated_types[indicator](form, key, value, section, survey)
            else:
                # Otherwise, save strings, floats, booleans.
                try:
                    value = float(value)
                except:
                    pass
                if value == 'on':
                    value = True
                survey.__getattribute__(section).__setattr__(key, value)


def _psr_from_value(form, key, value):
    """Save PotentiallySubjectiveResponse from a given value."""
    value_to_save = value
    if value == 'other':
        value_to_save = form.get('{}_other'.format(key), 'other (not specified)')
    return models.PotentiallySubjectiveResponse(
            value=value_to_save[:2000],
        subjective=questions.question_options[key][value]['subjective'] \
                if value in questions.question_options[key] else False
    )


def _save_gender_identity_coordinates(form, key, value, section, survey):
    """Save gender widget coordinates."""
    name = key[4:7]
    gic = models.GenderIdentityCoordinates(
        male=form.get('gic_{}_male'.format(name), ''),
        female=form.get('gic_{}_female'.format(name), ''),
        male_quantized=form.get('gic_{}_male_quantized'.format(name), ''),
        female_quantized=form.get('gic_{}_female_quantized'.format(name), ''),
    )
    question_name = {
        'exp': 'gender_expression_coords',
        'gid': 'gender_identity_coords',
        'gif': 'gender_in_furry_coords',
    }[name]
    survey.__getattribute__(section).__setattr__(question_name, gic)


def _save_number_per_option(form, key, value, section, survey):
    """Save number-per-option questions."""
    name = key[4:7]
    npo = models.NumberPerOption(
        option=key[8:],
        value=value
    )
    question_name = {
        'pol': 'political_views',
        'fac': 'furry_activities',
        'fao': 'furry_activities_opinion',
        'nfa': 'non_furry_activities',
        'imp': 'furry_importance',
        'bat': 'battery',
        'sim': 'sex_importance',
        'dvs': 'dom_or_sub',
    }[name]
    survey.__getattribute__(section).__getattribute__(question_name).append(npo)


def _save_string_per_option(form, key, value, section, survey):
    """Save string-per-option types."""
    name = key[4:7]
    spo = models.StringPerOption(
        option=key[8:],
        value=value
    )
    question_name = {
        'fws': 'furry_websites',
    }[name]
    survey.__getattribute__(section).__getattribute__(question_name).append(spo)


def _save_list_per_option(form, key, value, section, survey):
    """Save list-per-option types."""
    name = key[4:7]
    lpo = models.ListPerOption(
        option=key[8:],
        value=form.getlist(key)
    )
    question_name = {
        'int': 'interests',
    }[name]
    survey.__getattribute__(section).__getattribute__(question_name).append(lpo)


def _save_list_item(form, key, value, section, survey):
    """Append an item to a list."""
    name = key[4:7]
    question_name = {
        'con': 'conventions',
        'sds': 'self_described',
    }[name]
    values = form.getlist(key)
    survey.__getattribute__(section).__setattr__(question_name, values)


def _save_character(form, key, value, section, survey):
    """Save characters with metadata."""
    index = key.split('_')[1]

    # Since our form is immutable, we may wind up with additional responses;
    # If we've already saved this index, skip saving it again.
    if int(index) in map(lambda x: x.index, survey.overview.characters):
        return

    # Retrieve species data.
    species_category = form.getlist('chr_{}_category'.format(index))
    species_text = form.get('chr_{}_species'.format(index),
                            ', '.join(species_category))
    reason = form.get('chr_{}_reason'.format(index), '')
    primary_character = form.get('chr_{}_primary'.format(index), '') != ''
    deprecated_character = \
        form.get('chr_{}_deprecated'.format(index), '') != ''

    # Do not save blank species.
    if not species_category and not species_text:
        return
    survey.overview.characters.append(
        models.Character(
            index=index,
            species_category=species_category,
            species_text=models.PotentiallySubjectiveResponse(
                subjective=True,
                value=species_text[:2000]
            ),
            primary_character=primary_character,
            deprecated_character=deprecated_character,
            reason=models.PotentiallySubjectiveResponse(
                subjective=True,
                value=reason[:2000]
            )
        )
    )


def _save_raw_psr(form, key, value, section, survey):
    """Save raw text as a subjective response."""
    key = key[4:]
    survey.__getattribute__(section).__setattr__(
        key,
        models.PotentiallySubjectiveResponse(
            value=value[:2000],
            subjective=True))


if __name__ == '__main__':
    app.secret_key = 'Development key'
    app.debug = True
    app.config['SURVEY_ACTIVE'] = True
    app.run()
