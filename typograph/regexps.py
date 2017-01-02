import re

REPLACE_STRAIGHT_QUOTES_BY_GUILLEMETS = (re.compile(r'"([^"]*)"'), r'« \1 »')
# The : exception is here to make sure we don't add whitespaces around eg. http://
ADD_NBSP_BEFORE_PUNCTUATION = (re.compile(r'(?<![\xa0 ]) *((?:[?!»])|:(?= ))'), r' \1')
ADD_NBSP_AFTER_PUNCTUATION = (re.compile(r'(«) *(?![\xa0 ])'), r'\1 ')

BASE_REGEXPS = []
I18N_REGEXPS = {
    'fr': [
        REPLACE_STRAIGHT_QUOTES_BY_GUILLEMETS, ADD_NBSP_BEFORE_PUNCTUATION,
        ADD_NBSP_AFTER_PUNCTUATION,
    ]
}
