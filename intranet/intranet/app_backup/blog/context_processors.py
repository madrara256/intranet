from . models import (BlogPost)
import datetime
from django.utils import timezone

from . utils import memoize

def all_data(request):
    today = datetime.date.today()
    previous_day = today - (datetime.timedelta(days=14))
    num_of_days = datetime.timedelta(days=7)
    day_next_week =  today + num_of_days

    latest = today - (datetime.timedelta(minutes=30))

    time_now = datetime.datetime.now()
    time_ago = time_now - (datetime.timedelta(minutes=30))
    time_after = time_now + (datetime.timedelta(minutes=30))

    return {
    "communications_count":memoize(
    lambda: BlogPost.objects.all().count()
    ),
    "blogs":memoize(
    lambda: BlogPost.objects.filter(created_at__gt=previous_day, created_at__lt=day_next_week).order_by('-id')
    ),
    "communication_latest":memoize(
    lambda: BlogPost.objects.filter(created_at__gt=time_ago, created_at__lt=time_after)
    ),
    }
