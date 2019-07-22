"""intranet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .import views
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .import views  as website_views

app_name = 'website'


urlpatterns = [
    url(r'^$',views.all_news ,name='all_news'),
    url(r'^login/', auth_views.login, {'template_name': 'website/layout/login_template.html'}, name='login'),
    url(r'^login_redirect/', views.login_redirect),
    url(r'^admin/logout/$', auth_views.logout, name='logout'),
    url(r'^accounts/profile/', admin.site.urls, name='adminftb'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^save_profile/', views.save_profile, name='save_profile'),
    url(r'^edit_profile/', views.edit_profile, name='edit_profile'),
    url(r'^branch_directory/', views.branch_directory, name='branch_directory'),
    url(r'^staff_directory/', views.staff_directory, name='staff_directory'),
    url(r'^(?P<pk>[0-9]+)/', views.profile_view, name='profile_view'),
    url(r'^news/(?P<pk>[0-9]+)/', views.news_details, name='news_details'),
    url(r'^events/(?P<pk>[0-9]+)/', views.event_details, name='event_details'),
    url(r'^branch_news/(?P<pk>[0-9]+)/', views.branch_news, name='branch_news'),
    url(r'^home/', views.index, name='home'),
    url(r'^all_branch_news/', views.all_branch_news, name='all_branch_news'),
    url(r'^all_events/', views.all_events, name='all_events'),
    url(r'^all_announcements/', views.all_announcements, name='all_announcements'),
    url(r'^add_news/', views.add_news, name='add_news'),
    url(r'^post_news/', views.post_news, name='post_news'),
    url(r'^add_branch_news/', views.add_branch_news, name='add_branch_news'),
    url(r'^post_branch_news/', views.post_branch_news, name='post_branch_news'),
    url(r'^add_events/', views.add_events, name='add_events'),
    url(r'^post_event/', views.post_event, name='post_event'),
    url(r'^manage_data/', views.manage_data, name='manage_data'),
    url(r'^edit_event/(?P<pk>[0-9]+)/', views.edit_event, name='edit_event'),
    url(r'^delete_event/(?P<pk>[0-9]+)/', views.delete_event, name='delete_event'),
    url(r'^edit_news/(?P<pk>[0-9]+)/', views.edit_news, name='edit_news'),
    url(r'^delete_news/(?P<pk>[0-9]+)/', views.delete_news, name='delete_news'),
    url(r'^edit_branch_news/(?P<pk>[0-9]+)/', views.edit_branch_news, name='edit_branch_news'),
    url(r'^delete_branch_news/(?P<pk>[0-9]+)/', views.delete_branch_news, name='delete_branch_news'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
