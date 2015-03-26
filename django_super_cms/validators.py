# -*- coding:utf-8 -*-
# PROJECT_NAME : mysite
# FILE_NAME    : 
# AUTHOR       : younger shen
from django.contrib.auth import authenticate
from django_laravel_validator.validator import Validator
from .utils import captcha_validate
from .messages import CAPTCHA_INVALID
from .messages import USER_INVALID


class UserLoginValidator(Validator):
    username = 'required'
    password = 'required'
    captcha_0 = 'required'
    captcha_1 = 'required'

    def check(self):
        captcha_0 = self.get('captcha_0')
        captcha_1 = self.get('captcha_1')
        email = self.get('email')
        password = self.get('password')

        if not captcha_validate(captcha_0, captcha_1):
            self.add_error(dict(captcha=CAPTCHA_INVALID))
        else:
            user = authenticate(email=email, password=password)
            if not user:
                self.add_error(dict(user=USER_INVALID))
            else:
                setattr(self, 'user', user)