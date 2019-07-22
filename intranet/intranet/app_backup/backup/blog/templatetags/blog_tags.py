from django import template
from website.models import *
register = template.Library()

@register.simple_tag
def user_profile_image(pk):
    try:
        user_obj = Profile.objects.get(account_name=pk)
        user_image = user_obj.user_image
    except:
        user_image = ""

    return user_image

@register.filter('has_group')
def has_group(user, group_name):
    """ Verify if user belongs to group """
    groups = user.groups.all().values_list('name', flat=True)
    return True if group_name in groups else False
