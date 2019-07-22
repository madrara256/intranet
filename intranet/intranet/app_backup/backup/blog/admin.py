from django.contrib import admin
from . models import *
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
    'blog_title', 'created_by', 'department', 'created_at',
    )
    search_fields = [
    'blog_title', 'created_by',
    ]

admin.site.register(BlogPost, BlogPostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = (
    'comment_by', 'comment_date',
    )
admin.site.register(Comment, CommentAdmin)


class BlogFileAdmin(admin.ModelAdmin):
    list_display = (
    'file_title', 'file_type', 'file_post', 'posted_by', 'file', 'created_at',
    )
admin.site.register(BlogFile, BlogFileAdmin)
