"""Define handlers for each intent."""
from helpers import function_log, AppCheck
from responses import get_welcome_response, get_session_end_response, get_question_response


@AppCheck
def on_session_started(request, session):
    """ Called when the session starts """
    function_log('on_session_started', request, session)

@AppCheck
def on_launch(request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    function_log('on_launch', request, session)
    # Dispatch to your skill's launch
    return get_welcome_response()

@AppCheck
def on_intent(request, session):
    """ Called when the user specifies an intent for this skill """
    function_log('on_intent', request, session)

    intent = request['intent']
    intent_name = intent['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "QuestionAsked":
        return get_question_response(intent, session)
    elif intent_name == "AMAZON.HelpIntent" or not intent_name:
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return get_session_end_response()
    else:
        raise ValueError("Invalid intent")

@AppCheck
def on_session_ended(request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    function_log('on_session_started', request, session)
    # add cleanup logic here
