import os
from django.shortcuts import render, redirect, Http404
from django.http import HttpResponseRedirect, HttpResponse
from . models import *
from website.models import *
from documents.models import *
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from website.utils import check_group
# Create your views here.


def index(request):
    return render(request,'blog/layouts/index.html')

@check_group('Department Document Managers')
@login_required
def post_blog(request):
    if request.POST:
        error_message = "Please Check Internet Connection"
        success_message = "Communication posted"
        blog = BlogPost()
        if request.user is not None:
            blog.created_by = request.user
            if request.POST["blog_title"] and request.POST["blog_message"] and request.POST["department"]:
                blog.blog_title = request.POST["blog_title"]
                blog.blog_message = request.POST["blog_message"]
                blog.department = request.POST["department"]
                blog.created_by = request.user
                blog.save()
            try:
                blog_file = BlogFile()
                blog_file.file_title = blog.blog_title
                blog_file.posted_by = request.user
                blog_file.file_post = blog
                if request.POST["category"]:
                    blog_file.file_type = request.POST["category"]
                save_path = os.path.join(settings.MEDIA_ROOT, 'blog_files/')
                file = request.FILES["blog_file"]
                fs = FileSystemStorage()
                filename = fs.save('blog_files/'+file.name, file)
                blog_file.file = fs.url(filename)
                blog_file.save()
            except Exception as e:
                blog_file.file = ""
            messages.success(request, success_message)
            return redirect('blog:post_blog')
    return render(request,'blog/layouts/post_blog.html')

def get_blog(pk):
    context = {}
    try:
        blog = BlogPost.objects.get(id=pk)
        blog_comments = Comment.objects.filter(blog=blog).order_by('-id')
    except:
        blog = []
        blog_comments = []
    context['blog'] = blog
    context['blog_comments'] = blog_comments

    return context


def blog_view(request, pk):
    context = get_blog(pk)
    return render(request, 'blog/layouts/blog_view.html',context)



@login_required
def comment(request):
    if request.POST:
        success_message = "Comment Posted"
        blog_id = request.POST["blog_id"]
        comment = Comment()
        comment.blog = BlogPost.objects.get(id=blog_id)
        comment.comment_by = request.user
        comment.comment_text = request.POST["blog_comment"]
        comment.save()
        messages.success(request, success_message)
        context = get_blog(blog_id)
        return render(request, 'blog/layouts/blog_view.html',context)
    else:
        raise Http404

def manage_comms(request):
    context = {}
    blogs = BlogPost.objects.filter(created_by=request.user.id)
    context['blogs'] = blogs
    return render(request, 'blog/layouts/manage_commns.html', context)

def edit_blog(request, pk):
    context = get_blog(pk)
    if request.POST and request.user:
        if request.POST['blog_title'] and request.POST['blog_message']:
            blog = BlogPost.objects.get(id=pk)
            blog.blog_title = request.POST['blog_title']
            blog.blog_message = request.POST['blog_message']
            blog.save()
            return redirect('blog:manage_comms')
    return render(request, 'blog/layouts/edit_blog.html',context)

def delete_blog(request, pk):
    error_message = "Please Check Internet Connection"
    success_message = "Post Deleted"
    if request.user:
        blog = BlogPost.objects.get(id=pk)
        blog.delete()
        messages.success(request, success_message)
        return redirect('blog:manage_comms')
    else:
        messages.success(request, error_message)
        return redirect('blog:manage_comms')

def manage_data(request):
    return render(request, 'blog/layouts/manage_data.html')
