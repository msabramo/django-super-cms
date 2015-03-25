# -*- coding:utf-8 -*-
# PROJECT_NAME : django-super-cms
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_safe
from ..models import Post


def index(requesst):
    return HttpResponse('dsc')


@require_safe
def post_show_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return HttpResponse(post.id)


@require_safe
def post_list_view(request):
    pass