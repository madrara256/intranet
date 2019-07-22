import functools
from django.conf import settings
from functools import wraps
from django.shortcuts import redirect, Http404

def memoize(method):
    @functools.wraps(method)
    def memoizer(*args, **kwargs):
        method._cache = getattr(method, '_cache', {})
        key = args
        if key not in method._cache:
            method._cache[key] = method(*args, **kwargs)
        return method._cache[key]
    return memoizer

def check_group(group_name):
    def _check_group(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_anonymous:
                redirect('/')
            if (not (request.user.groups.filter(name=group_name).exists())):
                raise Http404
            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_group


def check_group_dup(group_name):
    def _check_group_dup(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if request.user.is_anonymous:
                redirect('/')
            if (not (request.user.groups.filter(name=group_name).exists())):
                raise Http404
            return view_func(request, *args, **kwargs)
        return wrapper
    return _check_group_dup
