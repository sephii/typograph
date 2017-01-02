# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import re

from bs4 import BeautifulSoup
import six

from .i18n import get_regexps_for_language
from .regexps import BASE_REGEXPS, I18N_REGEXPS


def format_html(html_content, regexps, html_parser):
    """
    Extract all strings from the given `html_content` and run the given list of `regexps` (see the documentation of
    :func:`format_text` for the regexps format. The `html_parser` argument is directly passed to BeautifulSoup as the
    parser to use.
    """
    parsed_html = BeautifulSoup(html_content, html_parser)
    strings = parsed_html.find_all(string=True)
    for string in strings:
        string.replace_with(format_text(string, regexps))

    if parsed_html.body:
        # lxml wraps everything in <html><body>, we need to strip that so we don't break the HTML
        new_html_content = ''.join(six.text_type(t) for t in parsed_html.body)
    else:
        new_html_content = six.text_type(parsed_html)

    return new_html_content


def format_text(content, regexps):
    """
    Run the given list of `regexps` which are expected to be `(regexp, replace)` tuples on the given `content`.
    """
    for search, replace in regexps:
        content = re.sub(search, replace, content)

    return content


def get_typograph(language_code, base_regexps=None, i18n_regexps=None, html_parser='html.parser'):
    """
    Return a formatting function based on the given language code and the given regexps. If `base_regexps` and
    `i18n_regexps` are not set, the default regexps defined in the `regexps` module are used.
    """
    if base_regexps is None:
        base_regexps = BASE_REGEXPS

    if i18n_regexps is None:
        i18n_regexps = I18N_REGEXPS

    regexps = get_regexps_for_language(language_code, base_regexps, i18n_regexps)

    def format(content, is_html=False):
        if is_html:
            return format_html(content, regexps, html_parser)
        else:
            return format_text(content, regexps)

    return format
