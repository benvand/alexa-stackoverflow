"""Helper functions to be used app wide."""

from HTMLParser import HTMLParser

import logging
import settings


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def function_log(function_name, request, session):
    logging.info("{function_name} requestId={request_id}, sessionId={session_id}".format(
        function_name=function_name,
        request_id=request.get('requestId', None),
        session_id=session.get('sessionId', None)
    ))


class AppCheck(object):
    def __init__(self, function):
        self.function = function

    def __call__(self, event, session):
        self.incoming_app_id = event['session']['application']['applicationId']
        # Prevent someone else from configuring a skill that sends requests to this
        # if not self.check_correct_app_id(self.incoming_app_id):
        #     raise ValueError("Invalid Application ID {app_id}".format(app_id=self.incoming_app_id))
        return self.function(event, session)

    def check_correct_app_id(self, id):
        """Ensure the incoming id matches our app id"""
        return self.incoming_app_id == settings.APP_ID


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
