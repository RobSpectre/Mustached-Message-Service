from random import choice

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request

from twilio import twiml

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')

# Constants
MUSTACHIFY_URL = "http://mustachify.me/?src="
LOADING_MESSAGES = [
        "Working on stashifying your pic...",
        "Please wait while we stash your photo...",
        "Our mustache engineers are assembling your pic now...",
        "Hang tight about 30 seconds for your mustache...",
        "Loading your mustache - please wait 30 seconds...",
        "We're almost there - now applying your mustache...",
        "Locating optimal mustache configuration - please wait...",
        "We're about to drop a stash bomb - loading...",
        "In a few moments, you'll have a sweet stash..."]
CAVEAT_MESSAGES = [
        "Missing a mustache? Try a frontal face photo.",
        "No stash? Try again with both eyes facing the camera.",
        "Did you get a mustache?  If not, try facing the camera fully.",
        "Stashing works best when you face the camera.",
        "No stash? Railer - try again facing the camera fully.",
        "For optimal mustache action, face the camera from the front."]
THANK_YOU_MESSAGES = [
        "Enjoying your stash?  Send this Twilio-powered phone number to your "
        "friends!",
        "Would you like to learn more about Twilio MMS? Go to "
        "http://www.twilio.com",
        "Sweet mustache?  Share this Twilio phone number with your friends!",
        "MUSTACHE ALL THE THINGS! Shoot these digits to your crew!",
        "This sweet stash was powered by Twilio - enjoy!",
        "Keep serving up the sweet upper lipholstery - send this Twilio number"
        " to your friends!",
        "No fun keeping the sweet stash action to yourself - send this Twilio "
        "number to your friends!"]
HELP_MESSAGES = [
        "Thank you for texting the Mustached Message Service from Twilio. Send"
        " me a selfie to get back a mustache.",
        "It's mustache time ya'll!  Send me a selfie to get back a stashed pic"
        " from Twilio MMS.",
        "Want a sweet mustache? Send me a selfie and get a stash applied by "
        "Twilio MMS.",
        "We're stashing people like crazy - send me a selfie to get back a "
        "mustache pic from Twilio MMS!",
        "Oh biscuits - you want a mustache?  Send me a photo of yourself and "
        "we'll send one from Twilio MMS!"]


# Voice Request URL
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    response = twiml.Response()
    response.say("Thank you for calling the Mustached Message Service."
                 "To score your sweet mustache, send a selfie to this "
                 "phone number.  Thank you and happy stashing from Twilio",
                 voice='alice')
    return str(response)


# SMS Request URL
@app.route('/sms', methods=['GET', 'POST'])
def sms():
    response = twiml.Response()

    if request.form['NumMedia'] != '0':
        response.message(choice(LOADING_MESSAGES))

        with response.message() as message:
            message.body = "{0} {1}".format(choice(CAVEAT_MESSAGES),
                                            choice(THANK_YOU_MESSAGES))
            message.media("{0}{1}".format(MUSTACHIFY_URL,
                                          request.form['MediaUrl0']))
    else:
        response.message(choice(HELP_MESSAGES))

    return str(response)


# Installation success page
@app.route('/')
def index():
    params = {
        'Voice Request URL': url_for('.voice', _external=True),
        'SMS Request URL': url_for('.sms', _external=True)}
    return render_template('index.html', params=params,
                           configuration_error=None)
