"""
This file effectively deals with routing the request. It's similar to a url router in that regard. Returning a given 
function based on the request type (as determined by Alexa).
I've proxied route to lambda_handler at the bottom to maintain consistent with Alexa documentation and examples. This
is the name of the function we give when setting up our lambda function. It's our 'Everything is to be routed through 
here' function
"""

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


