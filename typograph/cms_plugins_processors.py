from django.utils.safestring import mark_safe, SafeText
from djangocms_text_ckeditor.models import Text

from .django import get_django_typograph


def typograph_plugin(instance, placeholder, rendered_content, original_context):
    if not isinstance(instance, Text):
        return rendered_content

    new_html = get_django_typograph()(rendered_content, is_html=True)

    if isinstance(rendered_content, SafeText):
        return mark_safe(new_html)
    else:
        return new_html
