from django.contrib.auth import get_user_model
from django import template


register = template.Library()


@register.filter
def author_details(author):
    '''Returns {first_name}{last_name} if the user has entered any
    else returns only its username'''
    return f"{author.first_name} {author.last_name}" or f"{author.username}" \
        if isinstance(author, get_user_model()) \
        else ''
