# -*- coding:utf-8 -*-
# PROJECT_NAME : mysite
# FILE_NAME    : 
# AUTHOR       : younger shen

from django.conf.urls import patterns, include, url

# main views
urlpatterns = patterns('django_super_cms.views.main',
                       url(r'^$', 'index', name='')
                       )

# account views
# urlpatterns += patterns('django_super_cms.views.account',
#                         url(r'ss', '', name='')
#                         ),

# post views
urlpatterns += patterns('django_super_cms.views.post',
                        url(r'post/(?P<post_id>[0-9]+).html$', 'post_show_view', name='dsc_post_show_view')
                        )

# admin views
urlpatterns += patterns('django_super_cms.views.admin',
                        url(r'admin/index.html$', 'admin_index_view', name='dsc_admin_index_view'),
                        url(r'admin/login.html$', 'admin_login_view', name='dsc_admin_login_view')
                        )

# captcha
