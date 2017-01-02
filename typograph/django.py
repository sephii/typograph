from __future__ import absolute_import

from django.conf import settings
from django.utils.translation import get_language

from .regexps import BASE_REGEXPS, I18N_REGEXPS
from .typograph import get_typograph


def get_base_regexps():
    return getattr(settings, 'TYPOGRAPH_BASE_REGEXPS', BASE_REGEXPS)


def get_i18n_regexps():
    base_i18n_regexps = I18N_REGEXPS.copy()
    base_i18n_regexps.update(getattr(settings, 'TYPOGRAPH_I18N_REGEXPS', {}))

    return base_i18n_regexps


def get_html_parser():
    return getattr(settings, 'TYPOGRAPH_HTML_PARSER', 'html.parser')


def get_django_typograph():
    return get_typograph(get_language(), get_base_regexps(), get_i18n_regexps(), get_html_parser())
