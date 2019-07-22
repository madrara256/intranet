from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .import views

app_name = 'documents'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<pk>[0-9]+)/$', views.departmentFiles, name='department_files'),
        url(r'^(?P<pk>[0-9]+)/(?P<cat_id>[0-9]+)$', views.categoryFiles, name='category_files'),
        #url(r'^(?P<pk>[0-9]+)/$', views.departmentFiles, name='department_files'),
        #url(r'^app_details/$', views.applicationDetails, name='app_details'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
