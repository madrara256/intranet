from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'blog'

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^post_blog/', views.post_blog, name='post_blog' ),
        url(r'^blog/(?P<pk>[0-9]+)/', views.blog_view, name='blog_view'),
        url(r'^comment/', views.comment, name='comment'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
