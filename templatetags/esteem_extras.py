from django import template

register = template.Library()

@register.simple_tag
def can_add(object, user):
    if object is not None:
        if user is not None:
            return object.can_add(user)

@register.simple_tag
def can_view_in_list(object, user):
    if object is not None:
        if user is not None:
            return object.can_view_in_list(user)

@register.simple_tag
def can_list(object, user):
    if object is not None:
        if user is not None:
            return object.can_list(user)

@register.simple_tag
def can_view(object, user):
    if object is not None:
        if user is not None:
            return object.can_view(user)

@register.simple_tag
def can_change(object, user):
    if object is not None:
        if user is not None:
            return object.can_change(user)

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 
