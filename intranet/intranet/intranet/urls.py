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
from django.conf.urls import url, include, handler404, handler500
from django.contrib import admin
from documents import views as documents_views

admin.site.site_header = "Finance Trust Bank"
admin.site.site_title = "Finance Trust Bank Intranet"
admin.site.index_title = "Welcome to FTB Intranet"

urlpatterns = [
    url(r'^', include('website.urls', namespace='website')),
    url(r'^documents/', include('documents.urls', namespace='documents')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    #url(r'^analytics/', include('analytics.urls', namespace='analytics')),
    url(r'^admin/', admin.site.urls),
]

handler404 = 'documents.views.error_404'
handler500 = 'documents.views.error_500'
