# -*- coding:utf-8 -*-
# PROJECT_NAME : mysite
# FILE_NAME    : 
# AUTHOR       : younger shen

# customer user
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.core.mail import send_mail
from django.utils.translation import ugettext as _
from django.db import models
from .managers import UserManager
from .managers import SoftDeleteManager
import logging
logger = logging.getLogger('django_super_cms.models')
from unidecode import unidecode
import time


class AbstractUser(AbstractBaseUser, PermissionsMixin):

    USER_ACTIVED = 0
    USER_BLOCKED = 1
    USER_DEACTIVED = 2

    USER_STATUS_CHOICES = (
                             (USER_ACTIVED, 'Actived'),
                             (USER_BLOCKED, 'Blocked'),
                             (USER_DEACTIVED, 'Deactived')
                          )

    username = models.CharField(_('username'), max_length=255, unique=True)
    display_name = models.CharField(_('nickname'), max_length=25, unique=True)
    email = models.EmailField(_('user email address'), blank=True, null=True)
    url = models.URLField(_('user url'), max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('date updated'), auto_now=True)
    deleted_at = models.DateTimeField(_('date deleted'), blank=True, null=True)
    user_status = models.IntegerField(_('user status'), choices=USER_STATUS_CHOICES, default=USER_DEACTIVED)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()
    soft_objects = SoftDeleteManager()


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def get_full_name(self):
        return self.display_name if self.display_name else self.username

    def get_short_name(self):
        return self.get_full_name()

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_absolute_url(self):
        print self
        return ''


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'


class Entity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    soft_objects = SoftDeleteManager()

    class Meta:
        abstract = True


class Post(Entity):

    POST_SHOW = 0
    POST_HIDE = 1
    POST_DELETED = 2

    POST_TYPE_PAGE = 0
    POST_TYPE_POST = 1

    POST_STATUS_CHOICES = ((POST_SHOW, 'show'), (POST_HIDE, 'hide'), (POST_DELETED, 'deleted'))
    POST_TYPE_CHOICES = ((POST_TYPE_PAGE, 'page'), (POST_TYPE_POST, 'post'),)

    title = models.CharField(_('post title'), max_length=255)
    content = models.TextField(_('post content'))
    author_name = models.CharField(_('post author name'), max_length=255)
    author = models.ForeignKey(User, related_name='posts')
    status = models.IntegerField(_('post status'), choices=POST_STATUS_CHOICES, default=POST_SHOW)
    slug = models.CharField(_('post slug'), max_length=255)
    click = models.IntegerField(_('post click'), default=0)
    template_name = models.CharField(_('post templte name'), max_length=255)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True)
    post_type = models.IntegerField(_('post type'), choices=POST_TYPE_CHOICES, default=POST_TYPE_POST)

    def save(self, *args, **kwargs):

        if not self.author_name:
            self.author_name = self.author.get_full_name()

        if not self.slug:
            timestamp = int(time.time())
            self.slug = unidecode(self.title) + str(timestamp)

        if self.deleted_at:
            self.status = self.POST_DELETED

        if not self.template_name:
            self.template_name = 'page' if self.post_type == 0 else 'post'

        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = _('posts')
        verbose_name = _('post')
        ordering = ['-created_at', '-click']


class Comment(Entity):
    post = models.ForeignKey('Post', related_name='comments')
    author_name = models.CharField(_('author name'), max_length=255)
    author = models.ForeignKey(User, related_name='comments')
    author_url = models.CharField(_('author url'), max_length=255, blank=True, null=True)
    content = models.TextField(_('comment content'))
    is_approved = models.BooleanField(_('is comment approved'), default=False)
    parent = models.ForeignKey('self', related_name='children', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.author_name:
            self.author_name = self.author.get_full_name()

        if not self.author_url:
            self.author_url = self.author.geta_absolute_url()

        super(Comment, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('comment')
        verbose_name = _('comments')
        ordering = ['-created_at']