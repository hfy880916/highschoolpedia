# templatetags/nbsp.py

from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def linebreak(value):
    return mark_safe("&#10;".join(value.split('\n')))