"""Miscellaneous settings"""

from urlparse import urljoin
# Amazon application id
# Go to https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/handling-requests-sent-by-alexa
# Search for "Getting the Application ID for a Skill"
# https://developer.amazon.com/edw/home.html#/skills/list > edit > Application Id
#

# App settings
SITE_NAME = "stackoverflow"
SITE_NAME_SPEAKABLE = "Stack Overflow"


# URL Settings
BASE_API_URL = 'https://api.stackexchange.com/2.2/'
BASE_QUERY_PARAMS = '?order=asc&site={site_name}'.format(site_name=SITE_NAME)


ASK_QUESTION_ENDPOINT = BASE_API_URL + 'search/advanced' + BASE_QUERY_PARAMS + '&sort=score&q={question}'

GET_ANSWERS_ENDPOINT = BASE_API_URL + 'questions/{question_id}' + BASE_QUERY_PARAMS + '&sort=votes&filter=!*1ShIjGxdqfo8*16Wj*cAZl_Uj)x5F0ytNr2MbPmP'
