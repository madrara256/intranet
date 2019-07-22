from django.shortcuts import render, Http404, HttpResponse
from .models import *
from .filters import DocumentFilter

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

def error_404(request):
    return render(request, 'documents/error/error_404.html')

def error_500(request):
    return render(request, 'documents/error/error_500.html')
