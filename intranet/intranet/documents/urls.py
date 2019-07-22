from django.conf.urls import url, handler404, handler500
from django.conf import settings
from django.conf.urls.static import static

from .import views

app_name = 'documents'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^departments/', views.departments, name='departments'),
        url(r'^manage_documents/', views.manage_documents, name='manage_documents'),
        url(r'^add_department_docs/', views.add_department_docs, name='add_department_docs'),
        url(r'^add_quick_docs/', views.add_quick_docs, name='add_quick_docs'),
        url(r'^image_gallery/', views.view_image_gallery, name='image_gallery'),
        url(r'^(?P<pk>[0-9]+)/$', views.departmentFiles, name='department_files'),
        url(r'^(?P<pk>[0-9]+)/(?P<cat_id>[0-9]+)$', views.categoryFiles, name='category_files'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
