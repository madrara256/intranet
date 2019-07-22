import os
from django.shortcuts import render, redirect, Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from . models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . utils import check_group, check_group_dup

# Create your views here.

def index(request):
    return render(request,'website/layout/index.html')

def login_redirect(request):
    if request.user is not None:
        if request.user.is_superuser and request.user.is_active:
            return redirect('/accounts/profile/')
        else:
            try:
                user_profile = Profile.objects.get(account_name=request.user)
            except:
                return redirect('/profile/')

            if request.user.is_active and (user_profile.access_level == 2):
                return redirect('/accounts/profile/')
            elif request.user.is_active and (user_profile.access_level == 0):
                 return redirect('/profile/')
            elif request.user.is_active and (user_profile.access_level == 1):
                return redirect('/')
            else:
                redirect('website/layout/login_template.html')
    else:
        redirect('website/layout/login_template.html')

@login_required
def profile(request):
    return render(request,'website/layout/profile_template.html')


def save_profile(request):
    error_message = "Please Check Internet Connection"
    success_message = "Profile Created."
    if request.POST:
        if request.user is not None:
            try:
                save_path = os.path.join(settings.MEDIA_ROOT, 'user_images/')
                image = request.FILES['user_image']
                fs = FileSystemStorage()
                filename = fs.save('user_images/'+image.name, image)
                uploaded_file_url = fs.url(filename)
            except:
                uploaded_file_url = ""
            branch = Branch.objects.get(id=request.POST["branch"])
            department = Department.objects.get(id=request.POST["department"])
            user_profile = Profile(account_name=request.user)
            user_profile.branch = branch
            user_profile.department = department
            user_profile.user_bio = request.POST["user_bio"]
            user_profile.user_email = request.POST["user_email"]
            user_profile.user_telephone = request.POST["user_telephone"]
            user_profile.user_website = request.POST["user_website"]
            user_profile.user_facebook = request.POST["user_facebook"]
            user_profile.user_twitter = request.POST["user_twitter"]
            user_profile.user_linkedin = request.POST["user_linkedin"]
            user_profile.user_image = uploaded_file_url
            user_profile.full_name = request.user.first_name+" "+request.user.last_name
            user_profile.save()
            messages.success(request, success_message)
            return redirect('/')
        else:
            messages.success(request, error_message)
            return redirect('/profile/')

    else:
        return redirect('/profile/')

@login_required
def edit_profile(request):
    if request.POST and request.user:
        user_profile = Profile.objects.get(account_name=request.user)
        try:
            save_path = os.path.join(settings.MEDIA_ROOT, 'user_images/')
            image = request.FILES['user_image']
            fs = FileSystemStorage()
            filename = fs.save('user_images/'+image.name, image)
            uploaded_file_url = fs.url(filename)
            user_profile.user_image = uploaded_file_url
        except MultiValueDictKeyError:
            uploaded_file_url = user_profile.user_image
        if request.POST["user_birthday"]:
            user_profile.user_birthday = request.POST["user_birthday"]
        if request.POST["branch"]:
            branch = Branch.objects.get(id=request.POST["branch"])
            user_profile.branch = branch
        if request.POST["department"]:
            department = Department.objects.get(id=request.POST["department"])
            user_profile.department = department
        if request.POST["user_bio"]:
            user_profile.user_bio = request.POST["user_bio"]
        if request.POST["user_email"]:
            user_profile.user_email = request.POST["user_email"]
        if request.POST["user_telephone"]:
            user_profile.user_telephone = request.POST["user_telephone"]
        if request.POST["user_website"]:
            user_profile.user_website = request.POST["user_website"]
        if request.POST["user_facebook"]:
            user_profile.user_facebook = request.POST["user_facebook"]
        if request.POST["user_twitter"]:
            user_profile.user_twitter = request.POST["user_twitter"]
        if request.POST["user_linkedin"]:
            user_profile.user_linkedin = request.POST["user_linkedin"]
        user_profile.save()
        return redirect('/')
    return render(request, 'website/layout/edit_profile.html')

def branch_directory(request):
    return render(request, 'website/layout/branch_directory.html')

def staff_directory(request):
    return render(request, 'website/layout/staff_directory.html')

@login_required
def profile_view(request, pk=None):
    context = {}
    try:
        staff_profile = Profile.objects.get(id=pk)
    except:
        raise Http404
    context['staff_profile'] = staff_profile

    return render(request, 'website/layout/profile_view.html', context)

def news_details(request, pk=None):
    context = {}
    try:
        daily_news = News.objects.get(id=pk)
    except:
        raise Http404
    context['daily_news'] = daily_news
    return render(request, 'website/layout/news_details.html',context)

def event_details(request, pk=None):
    context = {}
    try:
        events = Event.objects.get(id=pk)
    except:
        raise Http404
    context['events'] = events
    return render(request, 'website/layout/event_details.html',context)

# def advert_details(request, pk=None):
#     context = {}
#     try:
#         adverts = Campaign.objects.get(id=pk)
#     except:
#         raise Http404
#     context['advert'] = adverts
#     return render(request, 'website/layout/advert_details.html',context)

def branch_news(request, pk=None):
    context = {}
    try:
        branch_news = BranchNews.objects.get(id=pk)
    except:
        raise Http404
    context['branch_news'] = branch_news
    return render(request, 'website/layout/branch_news.html',context)

def all_news(request):
    return render(request, 'website/layout/all_news.html')

def all_branch_news(request):
    return render(request, 'website/layout/all_branch_news.html')

def all_events(request):
    return render(request, 'website/layout/all_events.html')

def all_announcements(request):
    return render(request, 'website/layout/all_announcements.html')

@check_group('Content Managers')
@login_required
def add_news(request):
    return render(request, 'website/layout/add_news.html')

def post_news(request):
    error_message = "Please Check Internet Connection"
    success_message = "Article Posted"
    if request.POST and request.user:
        news = News()
        if request.POST["post_title"] and request.POST["post_message"]:
            news.title = request.POST["post_title"]
            news.message = request.POST["post_message"]
            news.created_by = request.user
        news.save()
        try:
            news_file = NewsFile()
            news_file.file_title = news.title
            news_file.file_post = news
            news_file.posted_by = request.user
            save_path = os.path.join(settings.MEDIA_ROOT, 'news_file/')
            file = request.FILES['news_file']
            fs = FileSystemStorage()
            filename = fs.save('news_files/'+file.name, file)
            news_file.file = fs.url(filename)
            if request.POST["category"]:
                news_file.file_type = request.POST["category"]
            news_file.save()
        except:
            news_file.file = ""
        messages.success(request, success_message)
        return redirect('website:add_news')
    else:
        messages.success(request, error_message)
        return redirect('website.add_news')


@check_group('Content Managers')
@login_required
def add_branch_news(request):
    return render(request, 'website/layout/add_branch_news.html')

def post_branch_news(request):
    error_message = "Please Check Internet Connection"
    success_message = "Article Posted."
    if request.POST and request.user:
        news = BranchNews()
        if request.POST["post_title"] and request.POST["post_message"] and request.POST["branch"]:
            news.title = request.POST["post_title"]
            news.message = request.POST["post_message"]
            news.branch = Branch.objects.get(id=request.POST["branch"])
            news.created_by = request.user
        news.save()
        try:
            news_file = BranchNewsFile()
            news_file.file_title = news.title
            news_file.file_post = news
            news_file.posted_by = request.user
            save_path = os.path.join(settings.MEDIA_ROOT, 'news_file/')
            file = request.FILES['news_file']
            fs = FileSystemStorage()
            filename = fs.save('news_files/'+file.name, file)
            news_file.file = fs.url(filename)
            if request.POST["category"]:
                news_file.file_type = request.POST["category"]
            news_file.save()
        except:
            news_file.file = ""
        messages.success(request, success_message)
        return redirect('website:add_branch_news')
    else:
        messages.success(request, error_message)
        return redirect('website.add_branch_news')

@check_group('Content Managers')
@login_required
def add_events(request):
    return render(request, 'website/layout/add_events.html')

def post_event(request):
    error_message = "Please Check Internet Connection"
    success_message = "Event Posted."
    if request.POST and request.user:
        event = Event()
        if request.POST["event_title"] and request.POST["event_message"] and request.POST["event_start_date"] and request.POST["event_end_date"] and request.POST["event_start_time"] and request.POST["event_end_time"] and request.POST["event_location"]:
            event.event_title = request.POST["event_title"]
            event.event_message = request.POST["event_message"]
            event.event_start_date = request.POST["event_start_date"]
            event.event_end_date = request.POST["event_end_date"]
            event.event_start_time = request.POST["event_start_time"]
            event.event_end_time = request.POST["event_end_time"]
            event.event_location = request.POST["event_location"]
            event.created_by = request.user
        event.save()
        try:
            event_file = EventFile()
            event_file.file_title = event.event_title
            event_file.file_post = event
            event_file.posted_by = request.user
            save_path = os.path.join(settings.MEDIA_ROOT, 'event_files/')
            file = request.FILES['event_file']
            fs = FileSystemStorage()
            filename = fs.save('event_files/'+file.name, file)
            event_file.file = fs.url(filename)
            if request.POST["category"]:
                event_file.file_type = request.POST["category"]
            event_file.save()
        except:
            event_file.file = ""
        messages.success(request, success_message)
        return redirect('website:add_events')
    else:
        messages.success(request, error_message)
        return redirect('website.add_events')
