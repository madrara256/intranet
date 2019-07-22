from django.db import models

# Create your models here.

class Organisation(models.Model):
    class Meta:
        verbose_name_plural = 'Finance Trust Bank Details'
    organisation_name = models.CharField(max_length=30)
    organisation_description = models.TextField(blank=False,null=False)
    organisation_mission = models.TextField(blank=False, null=False)
    organisation_vision = models.TextField(blank=False, null=False)
    organisation_location = models.CharField(max_length=200)
    organisation_postal_address = models.CharField(max_length=100)
    organisation_website = models.URLField(max_length=100)
    organisation_email = models.EmailField(max_length=100)
    organisation_contact = models.CharField(max_length=100)
    organisation_logo = models.FileField(upload_to='logo/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.organisation_name

class Branch(models.Model):
    class Meta:
        verbose_name_plural = 'Branches'

    branch_name = models.CharField(max_length=30)
    branch_location = models.CharField(max_length=100)
    branch_contact = models.CharField(max_length=100)
    branch_postal_address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.branch_name

class Department(models.Model):
    class Meta:
        verbose_name_plural = 'Departments'

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def resources(self):
        return self.document_set.all()

class DocumentCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Document Categories'

    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name



class Document(models.Model):
    class Meta:
        verbose_name_plural = 'Documents'

    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    document_category = models.ForeignKey('DocumentCategory', blank=True, null=True, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    document_icon = models.CharField(max_length=100, blank=True, null=True, default="fa fa-file-pdf-o")
    file = models.FileField(upload_to='department_documents/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    @property
    def resources(self):
        return self.document_set.all()

class Application(models.Model):
    application_name = models.CharField(max_length=100)
    short_decription = models.CharField(max_length=100, blank=True, null=True)
    application_url = models.CharField(max_length=200, blank=False, null=False)
    application_icon = models.CharField(max_length=100, blank=True, null=True, default="fa fa-gears")
    application_color = models.CharField(max_length=200, blank=True, null=True, default="#fff")
    application_logo = models.FileField(upload_to='logos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.application_name


class PublicDocument(models.Model):

    document_name = models.CharField(max_length=100)
    document_icon = models.CharField(max_length=100, blank=True, null=True, default="fa fa-file-pdf-o")
    document_file = models.FileField(upload_to='public/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document_name
