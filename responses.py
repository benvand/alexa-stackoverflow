"""Business logic to respond to a given request."""

import urllib2
import requests

from helpers import build_response, build_speechlet_response, strip_tags
import settings
import strings


def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = strings.WELCOME
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = strings.WELCOME_REPROMPT
    should_end_session = False
    speechlet_response = build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_response)

def get_session_end_response():
    card_title = "Session Ended"
    speech_output = strings.GOODBYE
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))

def get_question_response(intent, session):
    """ Finds the closes question, pulls the answer and reports back
    """
    card_title = intent['name']
    session_attributes = {}
    should_end_session = True
    speech_output = strings.FAILURE
    reprompt_text = strings.PROMPT_ASK

    if not 'QuestionAsked' in intent['slots']:
        speechlet_response = build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session)
        return build_response(session_attributes, speechlet_response)

    encoded_question = urllib2.quote(intent['slots']['QuestionAsked']['value'])

    url = settings.ASK_QUESTION_ENDPOINT.format(question=encoded_question)
    resp = requests.get(url).json()

    try:
        site_question = resp['items'][0]
    except (IndexError, KeyError):
        speech_output = strings.NO_QUESTIONS
        speechlet_response = build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session)
        return build_response(session_attributes, speechlet_response)

    site_question_question_id = site_question['question_id']
    site_question_title = site_question['title']

    url = settings.GET_ANSWERS_ENDPOINT.format(question_id=site_question_question_id)
    resp = requests.get(url).json()

    try:
        site_answer = sorted(resp['items']['answers'], key=lambda i: i['score'], reverse=True)[0]
    except (IndexError, KeyError):
        speech_output = strings.NO_ANSWERS
        speechlet_response = build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session)
        return build_response(session_attributes, speechlet_response)

    site_answer_answerer = site_answer['owner']['display_name']
    site_answer_score = site_answer['score']
    site_answer_body = strip_tags(site_answer['body'])


    speech_output = strings.REPORT.format(
        question=site_question_title,
        answerer=site_answer_answerer,
        votes=site_answer_score,
        answer=site_answer_body
    )
    speechlet_response = build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_response)