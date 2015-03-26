# -*- coding:utf-8 -*-
# PROJECT_NAME : django-super-cms
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.decorators.http import require_safe
from django_super_cms.utils import captcha_generator
from django_flash_message import storage
from ..models import Post


@login_required
def admin_index_view(request):
    return HttpResponse('admin page')


@require_safe
def admin_login_view(request):
    ret = dict()
    captcha = captcha_generator()
    ret.update(captcha)
    print ret
    return render(request, 'admin-ext/login.html', ret)