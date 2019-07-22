from django.contrib import admin
from . models import (
    Organisation, Branch, Department, DocumentCategory, Document, Application, PublicDocument
 )
# Register your models here.

class OrganisationAdmin(admin.ModelAdmin):
    list_display = (
     'organisation_name', 'organisation_location', 'organisation_postal_address',
     'organisation_website','organisation_email', 'organisation_contact', 'organisation_logo',
     'created_at', 'updated_at',
     )


    readonly_fields = (
     'created_at', 'updated_at',
     )

    fieldsets = (
     (None, {
         'fields':('organisation_name', 'organisation_description', 'organisation_mission', 'organisation_vision')
     }),
     ('More Details', {
         'classes': ('collapse',),
         'fields': (
             'organisation_location','organisation_postal_address',
             'organisation_website', 'organisation_email', 'organisation_contact',
             'organisation_logo', 'created_at', 'updated_at',
         ),
     }),
     )

admin.site.register(Organisation, OrganisationAdmin)

class BranchAdmin(admin.ModelAdmin):
    list_display = (
    'branch_name', 'branch_location', 'branch_contact',
     'branch_postal_address','created_at', 'updated_at',
    )
    readonly_fields = (
    'created_at', 'updated_at',
    )

admin.site.register(Branch, BranchAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = (
    'name', 'created_at', 'updated_at',
    )
    readonly_fields = (
    'created_at', 'updated_at',
    )
admin.site.register(Department, DepartmentAdmin)

class DocumentCategoryAdmin(admin.ModelAdmin):
     list_display = (
     'category_name', 'created_at', 'updated_at',
     )
     readonly_fields = (
     'created_at', 'updated_at',
     )
     search_fields = [
     'category_name',
     ]
admin.site.register(DocumentCategory, DocumentCategoryAdmin)

class DocumentAdmin(admin.ModelAdmin):
     list_display = (
     'file_name','department','document_icon', 'file', 'created_at', 'updated_at',
     )
     readonly_fields = (
     'created_at', 'updated_at',
     )
     search_fields = [
     'file_name', 'department__name',
     ]
admin.site.register(Document, DocumentAdmin)

class ApplicationAdmin(admin.ModelAdmin):
     list_display = (
     'application_name','application_url', 'application_icon', 'application_color', 'application_logo', 'created_at', 'updated_at',
     )
     readonly_fields = (
     'created_at', 'updated_at',
     )
     search_fields = [
     'application_name',
     ]
admin.site.register(Application, ApplicationAdmin)

class PublicDocumentAdmin(admin.ModelAdmin):
    list_display = (
    'document_name','document_icon', 'document_file', 'created_at', 'updated_at',
    )
    readonly_fields = (
    'created_at', 'updated_at',
    )
    search_fields = [
    'document_name',
    ]
admin.site.register(PublicDocument, PublicDocumentAdmin)
