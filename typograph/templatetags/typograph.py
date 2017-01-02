from django import template

from ..django import get_django_typograph

register = template.Library()


@register.filter(name='typograph_html')
def filter_html(value):
    return get_django_typograph()(value, is_html=True)


@register.filter(name='typograph_text')
def filter_text(value):
    return get_django_typograph()(value, is_html=False)
