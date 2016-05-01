"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import handlers


REQUEST_TYPE_HANDLERS = dict(
    new=handlers.on_session_started,
    LaunchRequest=handlers.on_launch,
    IntentRequest=handlers.on_intent,
    SessionEndedRequest=handlers.on_session_ended
)


def route(event, context):
    """Route a request to the correct handler based on it's request type"""
    if event['session']['new']:
        # Special case for new sessions.
        # Run this _as well_ as the desired request type handler
        REQUEST_TYPE_HANDLERS['new'](event, event['session'])
    request_type = event['request']['type']
    return REQUEST_TYPE_HANDLERS[request_type](event['request'], event['session'])

# This is named in our Amazon lambda function settings as the handler for this app
lambda_handler = route


