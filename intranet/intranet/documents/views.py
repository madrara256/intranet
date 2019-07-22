import os
from django.conf import settings
from django.shortcuts import render, Http404, HttpResponse, redirect
from .models import *
from .filters import DocumentFilter
from website.models import Profile
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'documents/layouts/index.html')

def departmentFiles(request, pk=None):
    context = {}
    try:
        department = Department.objects.get(id=pk)
        #
    except:
        raise Http404
    context['department'] = department
    return render(request, 'documents/layouts/department_files.html', context)

def categoryFiles(request, pk=None, cat_id=None):
    context = {}
    try:
        department = Department.objects.get(id=pk)
        category = DocumentCategory.objects.get(id=cat_id)
        #
    except:
        raise Http404
    documents = Document.objects.filter(department=department, document_category=category)
    context['cat_docs'] = documents
    context['department'] = department
    context['category'] = category
    return render(request, 'documents/layouts/cat_files.html', context)



def departments(request):
    return render(request, 'documents/layouts/departmental_docs.html')

def manage_documents(request):
    context = {}
    try:
        user_profile = Profile.objects.get(account_name=request.user.id)
        department_documents = Document.objects.filter(department=user_profile.department)
    except:
        raise Http404
    context['department_docs'] = department_documents
    return render(request, 'documents/layouts/manage_documents.html', context)


def add_department_docs(request):
    error_message = "Please check internet Connection"
    success_message = "Document Uploaded Successfully"
    if request.POST and request.user:
        user_department = Profile.objects.get(account_name=request.user.id)
        document = Document()
        if request.POST["category"] and request.POST["file_name"]:
            save_path = os.path.join(settings.MEDIA_ROOT, 'department_documents/')
            file = request.FILES['department_file']
            fs = FileSystemStorage()
            filename = fs.save('department_documents/'+file.name, file)
            document.file = fs.url(filename)
            document.department = Department.objects.get(id=user_department.department.id)
            document.document_category = DocumentCategory.objects.get(id=request.POST["category"])
            document.file_name = request.POST["file_name"]
            document.save()
            messages.success(request, success_message)
            return redirect('documents:manage_documents')
        else:
            messages.success(request, error_message)
            return redirect('documents.manage_documents')
    return render(request, 'documents/layouts/add_department_files.html')

def add_quick_docs(request):

        error_message = "Please check internet Connection"
        success_message = "Document Uploaded Successfully"
        if request.POST and request.user:
            user_department = Profile.objects.get(account_name=request.user.id)
            document = PublicDocument()
            if request.POST["file_name"]:
                save_path = os.path.join('', 'public/')
                file = request.FILES['department_file']
                fs = FileSystemStorage(location='public/')
                filename = fs.save('public/'+file.name, file)
                document.document_file = fs.url(filename)
                document.document_name = request.POST["file_name"]
                document.save()
                messages.success(request, success_message)
                return redirect('documents:manage_documents')
            else:
                messages.success(request, error_message)
                return redirect('documents.manage_documents')
        return render(request, 'documents/layouts/add_quick_documents.html')

def view_image_gallery(request, template_name='documents/layouts/image_gallery.html'):

    return render(request, template_name, locals())



def error_404(request):
    return render(request, 'documents/error/error_404.html')

def error_500(request):
    return render(request, 'documents/error/error_500.html')
