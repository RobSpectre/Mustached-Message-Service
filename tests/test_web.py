import unittest
from .context import app

app.config['TWILIO_ACCOUNT_SID'] = 'ACxxxxxx'
app.config['TWILIO_AUTH_TOKEN'] = 'yyyyyyyyy'
app.config['TWILIO_CALLER_ID'] = '+15558675309'
app.config['TWILIO_APP_SID'] = 'APzzzzzzzzzzzz'


class WebTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


class ExampleTests(WebTest):
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual("200 OK", response.status)
