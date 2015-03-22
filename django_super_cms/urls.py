# -*- coding:utf-8 -*-
# PROJECT_NAME : mysite
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns, include, url

urlpatterns = patterns('django_super_cms.views',
                       url(r'^$', 'index', name='')
                       )
