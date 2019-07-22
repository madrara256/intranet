from django.contrib import admin
from .models import (ImageAdvert, News, Event, Profile, BranchNews, NewsFile, BranchNewsFile, EventFile)
# Register your models here.

class ImageAdvertAdmin(admin.ModelAdmin):
    list_display = (
        'advert_title', 'run_from', 'run_to', 'created_by', 'created_at', 'advert_image',
    )
    readonly_fields = (
        'created_by', 'created_at',
    )
    search_fields = [
    'advert_title',
    ]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()

admin.site.register(ImageAdvert, ImageAdvertAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'created_by', 'created_at', 'last_modified_by', 'last_modified_at',
    )
    readonly_fields = (
     'created_by', 'created_at', 'last_modified_by', 'last_modified_at',
     )
    search_fields = [
     'title', 'created_by__username'
     ]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.last_modified_by = request.user
        obj.save()


admin.site.register(News, NewsAdmin)

class BranchNewsAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'created_by', 'created_at', 'last_modified_by', 'last_modified_at',
    )
    readonly_fields = (
     'created_by', 'created_at', 'last_modified_by', 'last_modified_at',
     )
    search_fields = [
     'title', 'created_by__username',
     ]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.last_modified_by = request.user
        obj.save()

admin.site.register(BranchNews, BranchNewsAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_title', 'event_start_date', 'event_end_date', 'event_location', 'created_by', 'created_at', 'last_modified_by', 'last_modified_at',
    )
    readonly_fields = (
     'created_by', 'created_at', 'last_modified_by', 'last_modified_at',
     )
    search_fields = [
     'event_title', 'created_by__username', 'event_location',
     ]

    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.last_modified_by = request.user
        obj.save()


admin.site.register(Event, EventAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'branch', 'department', 'office_title','user_email', 'user_telephone',
        'user_website', 'user_birthday', 'access_level', 'created_at', 'updated_at',
    )

    readonly_fields = (
    'full_name', 'account_name', 'office_title', 'user_website', 'user_email', 'user_telephone',
    'user_bio', 'user_birthday', 'created_at', 'updated_at',
    )

    search_fields = [
        'full_name', 'branch__branch_name','department__name', 'office_title',
    ]

    fieldsets = (
    (None, {
        'fields':('full_name', 'account_name', 'branch', 'department', 'office_title','access_level')
    }),
    ('View User Details', {
        'classes': ('collapse',),
        'fields': (
            'user_bio', 'user_telephone', 'user_email', 'user_website',
            'user_birthday', 'user_image', 'created_at', 'updated_at'
        ),
    }),
    )
admin.site.register(Profile, ProfileAdmin)

class NewsFileAdmin(admin.ModelAdmin):
    list_display = (
    'file_title', 'file_type', 'file_post', 'posted_by', 'file', 'created_at',
    )
admin.site.register(NewsFile,NewsFileAdmin)

class BranchNewsFileAdmin(admin.ModelAdmin):
    list_display = (
    'file_title', 'file_type', 'file_post', 'posted_by', 'file', 'created_at',
    )
admin.site.register(BranchNewsFile,BranchNewsFileAdmin)

class EventFileAdmin(admin.ModelAdmin):
    list_display = (
    'file_title', 'file_type', 'file_post', 'posted_by', 'file', 'created_at',
    )
admin.site.register(EventFile,EventFileAdmin)
