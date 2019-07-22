from django.db import models
from django.contrib.auth.models import User
from documents.models import Department
# Create your models here.

class BlogPost(models.Model):
    class Meta:
        verbose_name_plural = "Blog Posts"

    blog_title = models.CharField(max_length=255, null=True, blank=True)
    blog_message = models.TextField(null=False, blank=False)
    department = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='blog_entries_user')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title

class BlogFile(models.Model):
    class Meta:
        verbose_name_plural = "Blog Files"
    file_title = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    file_post = models.OneToOneField(BlogPost, on_delete=models.CASCADE, related_name='blog_files')
    posted_by = models.ForeignKey(User, blank=True, null=True)
    file = models.FileField(upload_to='blog_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_title

class Comment(models.Model):
    class Meta:
        verbose_name_plural = "Comments"
    blog = models.ForeignKey(BlogPost, null=True, blank=True, on_delete=models.CASCADE)
    comment_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='blog_comment_user')
    comment_text = models.TextField(null=True, blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.blog.blog_title
