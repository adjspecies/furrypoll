from flask import (
    Flask,
    g,
    session,
    redirect,
    render_template,
    request,
)
from flask.ext.mongoengine import MongoEngine

import datetime
import os

import models
import questions

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'furrypoll_2014'}
app.config["SECRET_KEY"] = os.urandom(12)
app.config["DEBUG"] = True

db = MongoEngine(app)

@app.route('/')
def front():
    return render_template('front.html')

@app.route('/survey/start/')
def surveyStart():
    """Begin a survey

    This view creates a response object if none exists and provides the user
    with some additional information about the survey.
    """
    if session.get('response_id', None) is not None:
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
    return render_template('start.html', survey_id=str(survey.id))

@app.route('/touch/question/<int:question_id>')
def surveyQuestion(question_id):
    """Mark a question answered

    This AJAX view marks a question as answered with a touchpoint, which is
    used to judge how quickly the respondent answered each question; spam
    responses generally take place far too quickly.
    """
    if session.get('response_id', None) is None:
        return '{error:"No session id"}'
    tp = models.Touchpoint(
        touchpoint_type=question_id
    )
    survey = models.Response.objects.get(id=session['response_id'])
    survey.metadata.touchpoints.append(tp)
    survey.save()
    return '{error:null}'

@app.route('/survey/overview/', methods=['GET', 'POST'])
def surveyOverview():
    """The Overview section of the survey"""
    if (session.get('response_id', None) is None):
        return redirect('/')
    survey = models.Response.objects.get(id=session['response_id'])
    if request.method == 'POST':
        tp = models.Touchpoint(
            touchpoint_type=-1
        )
        survey.metadata.touchpoints.append(tp)
        for key, value in request.form:
            if key in questions.question_options:
                if value == 'other':
                    value = request.form.pop('{}_other'.format(key), 'other (not specified)')
                psr = models.PotentiallySubjectiveresponse(
                    value=value,
                    subjective=questions.question_options[key][value].subjective
                )
                survey.overview.__setattr__(key, psr)
            else:
                indicator = key[:3]
                if indicator == 'gic':
                    name = key[4:7]
                    gic = models.GenderIdentityCoordinates(
                        male=request.form.pop('gic_{}_male'.format(name), ''),
                        female=request.form.pop('gic_{}_female'.format(name), ''),
                        male_quantized=request.form.pop('gic_{}_male_quantized'.format(name), ''),
                        female_quantized=equest.form.pop('gic_{}_female_quantized'.format(name), ''),
                    )
                    # TODO move to questions
                    question_name = {
                        'gic': 'gender_identity_coords',
                        'gif': 'gender_in_furry_coords',
                    }[name]
                    survey.overview.__setattr__(question_name, gic)
                elif indicator == 'npo':
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
                    }[name]
                    survey.overview.__getattribute__(question_name).append(npo)
                elif indicator == 'spo':
                    name = key[4:7]
                    spo = models.StringPerOption(
                        option=key[8:],
                        value=value
                    )
                    question_name = {
                        'fws': 'furry_websites',
                    }[name]
                    survey.overview.__getattribute__(question_name).append(spo)
                elif indicator == 'chr':
                    index = key[4:7]
                    species_category = request.form.pop('chr_{}_category'.format(index), '')
                    species_text = request.form.pop('chr_{}_species'.format(index), species_category)
                    reason = request.form.pop('chr_{}_reason'.format(index), '')
                    character = models.Character(
                        species_category=species_category,
                        species_text=models.PotentiallySubjectiveResponse(
                            subjective=True,
                            value=species_text
                        ),
                        reason=models.PotentiallySubjectiveResponse(
                            subjective=True,
                            value=reason
                        )
                    )
                    survey.overview.characters.append(character)
                else:
                    survey.overview.__setattr__(key, value)
        survey.save()
        return redirect('/survey/psychographic/')
    else:
        if -1 in [tp.touchpoint_type for tp in survey.metadata.touchpoints]:
            return redirect('/survey/psychographic/')
        return render_template('overview.html', questions=questions)

@app.route('/survey/psychographic/', methods=['GET', 'POST'])
def surveyPsychographic():
    """The Psychographic Battery section of the survey"""
    survey = models.Response.objects.get(id=session['response_id'])
    if request.method == 'POST':
        tp = models.Touchpoint(
            touchpoint_type=-2
        )
        survey.metadata.touchpoints.append(tp)
        # save answers
        survey.save()
        return redirect('/survey/sexuality/')
    else:
        import pdb; pdb.set_trace()
        if -2 in [tp.touchpoint_type for tp in survey.metadata.touchpoints]:
            return redirect('/survey/sexuality/')
        return render_template('psychographic.html')

@app.route('/survey/sexuality/', methods=['GET', 'POST'])
def surveySexuality():
    """The Sexuality section of the survey"""
    survey = models.Response.objects.get(id=session['response_id'])
    if request.method == 'POST':
        tp = models.Touchpoint(
            touchpoint_type=-3
        )
        survey.metadata.touchpoints.append(tp)
        # save answers
        survey.save()
        return redirect('/survey/complete/')
    else:
        if -3 in [tp.touchpoint_type for tp in survey.metadata.touchpoints]:
            return redirect('/survey/complete/')
        return render_template('sexuality.html')

@app.route('/survey/complete/')
def surveyComplete():
    """Mark a survey as complete"""
    survey = models.Response.objects.get(id=session['response_id'])
    if -4 not in [tp.touchpoint_type for tp in survey.metadata.touchpoints]:
        tp = models.Touchpoint(
            touchpoint_type=-4
        )
        survey.metadata.touchpoints.append(tp)
        survey.save()
    return render_template('complete.html')

@app.route('/survey/cancel/')
def surveyCancel():
    """Mark a survey as canceled"""
    survey = models.Response.objects.get(id=session['response_id'])
    tp = models.Touchpoint(
        touchpoint_type=-5
    )
    survey.metadata.touchpoints.append(tp)
    survey.save()
    session['response_id'] = None
    return render_template('cancel.html')

if __name__ == '__main__':
    app.secret_key = 'Development key'
    app.run()
