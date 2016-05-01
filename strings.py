from settings import SITE_NAME_SPEAKABLE

SITE_NAME = SITE_NAME_SPEAKABLE

# Breaks
BREAK = '<break strength="{strength}">'
XS_BREAK = BREAK.format(strength='x-strong')
S_BREAK = BREAK.format(strength='strong')



# Greet and dismiss
WELCOME_REPROMPT = \
"""
You can ask {site_name} for an answer to a question.
For example, try, Ask {site_name}{break1} what is node j s.
""".format(site_name=SITE_NAME, break1=S_BREAK)

WELCOME = ("Welcome to the Alexa {site_name} Skill. " + WELCOME_REPROMPT).format(site_name=SITE_NAME)
GOODBYE = "Thank you for trying the Alexa {site-name}.".format(site_name=SITE_NAME)

# Humanisation string
SEARCHING = 'Searching ' + SITE_NAME + ' for {question} '

# Report of what has been found
REPORT_ON_QUESTION = "The closest question on" + SITE_NAME + ' is {question}'
REPORT_ON_ANSWER = SEARCHING + "The top rated article on " + SITE_NAME + " by {answerer} with {votes} upvotes is {answer}."
REPORT = S_BREAK.join(REPORT_ON_QUESTION, REPORT_ON_ANSWER)

# Failure to parse and reprompt
FAILURE = "I'm sorry, I didn't catch your question. Please try again."
PROMPT_ASK = "Your questions will be relayed to {site_name}."

# Nothing found responses
NO_QUESTIONS = SEARCHING + "I'm sorry, that didn't return any results on {site_name}."
NO_ANSWERS = NO_QUESTIONS + "However there is a question waiting to be answered."
