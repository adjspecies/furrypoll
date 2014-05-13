from flask import (
    Flask,
    g,
    session,
    render_template,
    request,
)
from flask.ext.mongoengine import MongoEngine

import os
import datetime

import models

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
    # create document, store id, survey start touchpoint, store ip, ua
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
    return render_template('start.html')

@app.route('/touch/question/<int:question_id>')
def surveyQuestion(question_id):
    # store a touchpoint that a question was answered
    tp = models.Touchpoint(
        touchpoint_type=question_id
    )
    survey = models.Response.objects.get(id=session['response_id'])
    survey.metadata.touchpoints.append(tp)
    survey.save()
    return '{error:null}'

@app.route('/survey/overview/')
def surveyOverview():
    survey = models.Response.objects.get(id=session['response_id'])
    if request.method == 'POST':
        tp = models.Touchpoint(
            toucpoint_type=-1
        )
        survey.metadata.touchpoints.append(tp)
        # save answers
        survey.save()
        # redirect to psychographic
    else:
        return render_template('overview.html')

@app.route('/survey/psychographic/')
def surveyPsychographic():
    survey = models.Response.objects.get(id=session['response_id'])
    if request.method == 'POST':
        tp = models.Touchpoint(
            toucpoint_type=-2
        )
        survey.metadata.touchpoints.append(tp)
        # save answers
        survey.save()
        # redirect to sexuality
    else:
        return render_template('psychographic.html')

@app.route('/survey/sexuality/')
def surveySexuality():
    survey = models.Response.objects.get(id=session['response_id'])
    if request.method == 'POST':
        tp = models.Touchpoint(
            toucpoint_type=-3
        )
        survey.metadata.touchpoints.append(tp)
        # save answers
        survey.save()
        # redirect to sexuality
    else:
        return render_template('psychographic.html')

@app.route('/survey/complete/')
def surveyComplete():
    survey = models.Response.objects.get(id=session['response_id'])
    tp = models.Touchpoint(
        touchpoint_type=-4
    )
    survey.metadata.touchpoints.append(tp)
    survey.save()
    return render_template('complete.html')

@app.route('/survey/cancel/')
def surveyCancel():
    survey = models.Response.objects.get(id=session['response_id'])
    tp = models.Touchpoint(
        touchpoint_type=-5
    )
    survey.metadata.touchpoints.append(tp)
    survey.save()
    return render_template('cancel.html')

if __name__ == '__main__':
    app.secret_key = 'Development key'
    app.run()
