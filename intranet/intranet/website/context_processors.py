from . models import (News, Event, ImageAdvert, Profile, BranchNews)
import datetime
from django.utils import timezone

from . utils import memoize

def all_news(request):
    today = datetime.date.today()
    previous_day = today - (datetime.timedelta(days=7))
    num_of_days = datetime.timedelta(days=7)
    day_next_week =  today + num_of_days

    return {

    "news":memoize(
    lambda: News.objects.filter(created_at__gt=previous_day, created_at__lt=day_next_week).order_by('created_at').reverse()
    ),

    "branch_news": memoize(
    lambda: BranchNews.objects.filter(created_at__gt=previous_day, created_at__lt=day_next_week).order_by('created_at').reverse()
    ),

    "archive_all_news": memoize(
    lambda: News.objects.filter(created_at__lt=previous_day).order_by('created_at').reverse()[:30]
    ),

    "archive_branch_news": memoize(
    lambda: BranchNews.objects.filter( created_at__lt=previous_day).order_by('created_at').reverse()[:30]
    ),

    "branch_news_count": memoize(
    lambda: BranchNews.objects.filter().count()
    ),
    }

def all_events(request):
    date_today = datetime.date.today()
    return {
    "events":memoize(
    lambda:Event.objects.filter(event_start_date__gte=date_today)
    ),
    "events_count":memoize(
    lambda:Event.objects.filter(event_start_date__gte=date_today).count()
    ),
    }

def all_adverts(request):
    date_today = datetime.date.today()
    return {
    "adverts":memoize(
    lambda:ImageAdvert.objects.filter(run_to__gt=date_today).order_by('-id')
    ),
    }

def get_user_profile(request):
    if request.user is None:
        return
    else:
        return{
        "user_profile":memoize(
        lambda:Profile.objects.get(account_name=request.user)
        ),
        }
def get_staff(request):
    return {
    "users": memoize(
    lambda:Profile.objects.all()
    ),
    }
