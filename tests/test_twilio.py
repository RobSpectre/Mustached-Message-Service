import unittest
from .context import app


app.config['TWILIO_ACCOUNT_SID'] = 'ACxxxxxx'
app.config['TWILIO_AUTH_TOKEN'] = 'yyyyyyyyy'
app.config['TWILIO_CALLER_ID'] = '+15558675309'


class TwiMLTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def assertTwiML(self, response):
        app.logger.info(response.data)
        self.assertTrue(b"</Response>" in response.data, "Did not find "
                        "</Response>: {0}".format(response.data))
        self.assertEqual("200 OK", response.status)

    def sms(self, body, url='/sms', to=app.config['TWILIO_CALLER_ID'],
            from_='+15558675309', extra_params=None):
        params = {
            'SmsSid': 'SMtesting',
            'AccountSid': app.config['TWILIO_ACCOUNT_SID'],
            'To': to,
            'From': from_,
            'Body': body,
            'FromCity': 'BROOKLYN',
            'FromState': 'NY',
            'FromCountry': 'US',
            'FromZip': '55555'}
        if extra_params:
            params = dict(list(params.items()) + list(extra_params.items()))
        return self.app.post(url, data=params)

    def call(self, url='/voice', to=app.config['TWILIO_CALLER_ID'],
             from_='+15558675309', digits=None, extra_params=None):
        params = {
            'CallSid': 'CAtesting',
            'AccountSid': app.config['TWILIO_ACCOUNT_SID'],
            'To': to,
            'From': from_,
            'CallStatus': 'ringing',
            'Direction': 'inbound',
            'FromCity': 'BROOKLYN',
            'FromState': 'NY',
            'FromCountry': 'US',
            'FromZip': '55555'}
        if digits:
            params['Digits'] = digits
        if extra_params:
            params = dict(list(params.items()) + list(extra_params.items()))
        return self.app.post(url, data=params)


class ExampleTests(TwiMLTest):
    def test_voice(self):
        response = self.call()
        self.assertTwiML(response)


class MustacheTests(TwiMLTest):
    def test_no_photo(self):
        response = self.sms("Testing.", extra_params={'NumMedia': '0'})
        self.assertTwiML(response)
        self.assertTrue(b'<Message>' in response.data, "Did not find a help "
                        "message in response: {0}".format(response.data))
        self.assertFalse(b'<Media>' in response.data, "Found a <Media> noun "
                        "in help message: {0}".format(response.data))

    def test_photo(self):
        response = self.sms("Testing", extra_params={
                            'MediaUrl0': "http://example.com/pic.png",
                            'NumMedia': '1'})
        self.assertTwiML(response)
        self.assertTrue(b'<Media>' in response.data, "Did not return stashed "
                        "photo: {0}".format(response.data))
        self.assertTrue(b'<Body>' in response.data, "Did not return message "
                        "with stash: {0}".format(response.data))
        self.assertTrue(b'<Message>' in response.data, "Did not return loading"
                        " message with stash response: "
                        "{0}".format(response.data))
