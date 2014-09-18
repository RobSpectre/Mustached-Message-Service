# Mustached Message Service 

A Flask app demonstrating [Twilio MMS](http://www.twilio.com/mms) through facial recognition/hair.

See it by sending a selfie to one of these numbers!

* US - (646) 846-8238
* Canada - (438) 793-8863

[![Build
Status](https://secure.travis-ci.org/RobSpectre/Mustached-Message-Service.png)]
(http://travis-ci.org/RobSpectre/Mustached-Message-Service)
[![Coverage Status](https://coveralls.io/repos/RobSpectre/Mustached-Message-Service/badge.png)]
(https://coveralls.io/r/RobSpectre/Mustached-Message-Service)


Deploy this hackpack to Heroku now!

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/RobSpectre/Mustached-Message-Service)



## Usage

This hack ships with two ready-to-go endpoints for your Twilio Voice and SMS
apps.  The two routes /voice and /sms contain two examples you can modify
easily.

To start tweaking your hackpack, just edit `hackpack/app.py`.

To give it a try, configure your Twilio number's Messaging Request URL to the
`/sms` endpoint.


## Installation

Step-by-step on how to deploy, configure and develop on this hackpack.

### Fastest Deploy

Use Heroku to deploy this hackpack immediately:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy?template=https://github.com/RobSpectre/Mustached-Message-Service)

### Getting Started 

1) Grab latest source
<pre>
git clone git://github.com/RobSpectre/Mustached-Message-Service.git 
</pre>

2) Navigate to folder and create new Heroku Cedar app
<pre>
heroku create
</pre>

3) Deploy to Heroku
<pre>
git push heroku master
</pre>

4) Scale your dynos
<pre>
heroku scale web=1
</pre>

5) Visit the home page of your new Heroku app to see your newly configured app!
<pre>
heroku open
</pre>


### Configuration

Want to use the built-in Twilio Client template?  Configure your hackpack with
three easy options.

#### Automagic Configuration

This hackpack ships with an auto-configure script that will create a new TwiML
app, purchase a new phone number, and set your Heroku app's environment
variables to use your new settings.  Here's a quick step-by-step:

1) Make sure you have all dependencies installed
<pre>
make init
</pre>

2) Run configure script and follow instructions.
<pre>
python configure.py --account_sid ACxxxxxx --auth_token yyyyyyy
</pre>

3) For local development, copy/paste the environment variable commands the
configurator provides to your shell.
<pre>
export TWILIO_ACCOUNT_SID=ACxxxxxx
export TWILIO_AUTH_TOKEN=yyyyyyyyy
export TWILIO_APP_SID=APzzzzzzzzzz
export TWILIO_CALLER_ID=+15556667777
</pre>

Automagic configuration comes with a number of features.  
`python configure.py --help` to see them all.


#### local_settings.py

local_settings.py is a file available in the hackpack route for you to configure
your twilio account credentials manually.  Be sure not to expose your Twilio
account to a public repo though.

```python
ACCOUNT_SID = "ACxxxxxxxxxxxxx" 
AUTH_TOKEN = "yyyyyyyyyyyyyyyy"
TWILIO_APP_SID = "APzzzzzzzzz"
TWILIO_CALLER_ID = "+17778889999"
```

#### Setting Your Own Environment Variables

The configurator will automatically use your environment variables if you
already have a TwiML app and phone number you would prefer to use.  When these
environment variables are present, it will configure the Twilio and Heroku apps
all to use the hackpack.

1) Set environment variables locally.
<pre>
export TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxx
export TWILIO_AUTH_TOKEN=yyyyyyyyyyyyyyyyy
export TWILIO_APP_SID=APzzzzzzzzzzzzzzzzzz
export TWILIO_CALLER_ID=+15556667777
</pre>

2) Run configurator
<pre>
python configure.py
</pre>


### Development

Getting your local environment setup to work with this hackpack is similarly
easy.  After you configure your hackpack with the steps above, use this guide to
get going locally:

1) Install the dependencies.
<pre>
make init
</pre>

2) Launch local development webserver
<pre>
foreman start
</pre>

3) Open browser to [http://localhost:5000](http://localhost:5000).

4) Tweak away on `hackpack/app.py`.


## Testing

This hackpack comes with a full testing suite ready for nose.

<pre>
make test
</pre>

It also ships with an easy-to-use base class for testing your
[TwiML](http://www.twilio.com/docs/api/twiml).  For example, testing a basic SMS
response is only two lines of code:

```python
import test_twilio

class ExampleTest(test_twilio.TwiMLTest):
    response = self.sms("Test")
    self.assertTwiML(response)
```

You can also test your [Gather
verbs](http://www.twilio.com/docs/api/twiml/gather) for voice apps very easily.

```python
import test_twilio

class ExampleTest(test_twilio.TwiMLTest):
    response = self.call(digits="1")
    self.assertTwiML(response)
```


## Branches

Two configurations are available in different branches:

* master - Default dev mode with minimum possible code to get going.
* production - Intended for live use with more code and dependencies appropriate
  to a production environment. To deploy this branch instead, adjust your
  procedure for the production branch:

<pre>
git checkout production
git push heroku production:master
</pre>


## Meta 

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by [Twilio New
 York](http://www.meetup.com/Twilio/New-York-NY/) 


## Community Contributors

Here we recognize crack members of the Twilio community who worked on this
hackpack.

* [Timothée Boucher](http://www.timotheeboucher.com/) - idea for production
  branch
* [Oscar](http://labcoder.com/) - Bug fix for user input
* [Zachary
  Woase](http://zacharyvoase.com/) - [Twilio signature
  validation](https://github.com/RobSpectre/Mustached-Message-Service/pull/7) for production branch.
* [Kevin Burke](http://www.twentymilliseconds.com/) - Better FTU for Twilio
  Client.


[![githalytics.com
alpha](https://cruel-carlota.pagodabox.com/33a5ddd61dd29dd933422bca2b3dfa0e
"githalytics.com")](http://githalytics.com/RobSpectre/Mustached-Message-Service)
