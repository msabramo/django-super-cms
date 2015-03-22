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
from django_super_cms.managers import UserManager


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


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
