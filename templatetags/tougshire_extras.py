from django import template
import os

register = template.Library()

@register.simple_tag
def get_field_label(object, fieldname):
    try:
        return object._meta.get_field(fieldname).verbose_name.capitalize
    except:
        return "=="

@register.filter
def dollar(amount):
    if amount is None:
        return ''

    return '${:.2f}'.format(amount)

@register.filter
def filename(filepath):
    return os.path.split(filepath)[1]
