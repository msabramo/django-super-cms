# -*- coding:utf-8 -*-
# PROJECT_NAME : mysite
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns, include, url

urlpatterns = patterns('django_super_cms.views.main',
                       url(r'^$', 'index', name='')
                       )

# urlpatterns += patterns('django_super_cms.views.account',
#                         url(r'ss', '', name='')
#                         ),

urlpatterns += patterns('django_super_cms.views.post',
                        url(r'^post/(?P<post_id>[0-9]+)/$', 'post_show_view', name='dsc_post_show_view')
                        )