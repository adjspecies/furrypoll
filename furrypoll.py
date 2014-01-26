from flask import (
    Flask,
    g,
    session,
    render_template,
)
from flask.ext.mongoengine import MongoEngine

import os

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': 'furrypoll_2014'}
app.config["SECRET_KEY"] = os.urandom(12)

db = MongoEngine(app)

@app.route('/')
def front():
    return render_template('templates/front.html')

@app.route('/survey/start/')
def surveyStart():
    # create document, store id, survey start touchpoint, store ip, ua
    pass

@app.route('/survey/overview/')
def surveyOverview():
    pass

@app.route('/survey/psychographic/')
def surveyPsychographic():
    pass

@app.route('/survey/sexuality/')
def surveySexuality():
    pass

@app.route('/survey/complete/')
def surveyComplete():
    pass

if __name__ == '__main__':
    app.secret_key = 'Development key'
    app.run()
