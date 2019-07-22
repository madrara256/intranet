from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views
app_name = 'blog'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^post_blog/', views.post_blog, name='post_blog' ),
        url(r'^manage_comms/', views.manage_comms, name='manage_comms' ),
        url(r'^manage_data/', views.manage_data, name='manage_data' ),
        url(r'^edit_blog/(?P<pk>[0-9]+)/', views.edit_blog, name='edit_blog'),
        url(r'^delete_blog/(?P<pk>[0-9]+)/', views.delete_blog, name='delete_blog'),
        url(r'^blog/(?P<pk>[0-9]+)/', views.blog_view, name='blog_view'),
        url(r'^comment/', views.comment, name='comment'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
