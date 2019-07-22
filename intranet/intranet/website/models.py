from django.db import models
from django.contrib.auth.models import User
from documents.models import *

# Create your models here.

class ImageAdvert(models.Model):
    class Meta:
        verbose_name_plural = "Image Adverts"

    advert_title = models.CharField(max_length=255, blank=True, null=True)
    run_from = models.DateTimeField(blank=True, null=True)
    run_to = models.DateTimeField(blank=True, null=True)
    advert_image = models.FileField(upload_to='advert_image/', blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='advert_entries')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.advert_title

class News(models.Model):
    class Meta:
        verbose_name_plural = "News / Annoucements"

    title = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='news_entries')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='news_entry_modifiers')
    last_modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    class Meta:
        verbose_name_plural = "Events"

    event_title = models.CharField(max_length=255, blank=True, null=True)
    event_message = models.TextField(blank=True, null=True)
    event_start_date = models.DateField(blank=True, null=True)
    event_end_date = models.DateField(blank=True, null=True)
    event_start_time = models.CharField(max_length=100, blank=True, null=True)
    event_end_time = models.CharField(max_length=100, blank=True, null=True)
    event_location = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='event_entries')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='event_entry_modifiers')
    last_modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_title

    def event_start_year(self):
        return self.event_start_date.strftime('%Y')
    def event_start_month(self):
        return self.event_start_date.strftime('%n')
    def event_start_day(self):
        return self.event_start_date.strftime('%d')

    def event_end_year(self):
        return self.event_end_date.strftime('%Y')
    def event_end_month(self):
        return self.event_end_date.strftime('%n')
    def event_end_day(self):
        return self.event_end_date.strftime('%d')


class Profile(models.Model):
    class Meta:
        verbose_name_plural = 'User Profiles'
    account_name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    full_name = models.CharField(max_length=255, default="N/A")
    access_level = models.PositiveSmallIntegerField(default=1)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='user_branch', blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='user_department', blank=True, null=True)
    office_title = models.CharField(max_length=255, blank=True, null=True)
    user_bio = models.TextField(blank=True, null=True)
    user_telephone = models.CharField(max_length=255, blank=True, null=True)
    user_email = models.EmailField(max_length=255, blank=True, null=True)
    user_website = models.URLField(max_length=255, blank=True, null=True)
    user_facebook = models.URLField(max_length=255, blank=True, null=True)
    user_twitter = models.URLField(max_length=255, blank=True, null=True)
    user_linkedin = models.URLField(max_length=255, blank=True, null=True)
    user_image = models.FileField(upload_to='user_images/', blank=True, null=True)
    user_birthday = models.DateField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class BranchNews(models.Model):
    class Meta:
        verbose_name_plural = "Happening At Branches"

    title = models.CharField(max_length=255, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='news_branch', blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='branch_news_entries')
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='branch_news_entry_modifiers')
    last_modified_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NewsFile(models.Model):
    class Meta:
        verbose_name_plural = "News Files"
    file_title = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    file_post = models.OneToOneField(News, on_delete=models.CASCADE, related_name='news_file')
    posted_by = models.ForeignKey(User, blank=True, null=True)
    file = models.FileField(upload_to='news_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_title

class BranchNewsFile(models.Model):
    class Meta:
        verbose_name_plural = "Branch News Files"
    file_title = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    file_post = models.OneToOneField(BranchNews, on_delete=models.CASCADE, related_name='branch_news_file')
    posted_by = models.ForeignKey(User, blank=True, null=True)
    file = models.FileField(upload_to='branch_news_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_title

class EventFile(models.Model):
    class Meta:
        verbose_name_plural = "Event Files"
    file_title = models.CharField(max_length=255, blank=True, null=True)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    file_post = models.OneToOneField(Event, on_delete=models.CASCADE, related_name='event_files')
    posted_by = models.ForeignKey(User, blank=True, null=True)
    file = models.FileField(upload_to='event_files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_title
