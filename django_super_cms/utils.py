# -*- coding:utf-8 -*-
# PROJECT_NAME : mysite
# FILE_NAME    : 
# AUTHOR       : younger shen
from captcha.models import CaptchaStore
from captcha.models import get_safe_now


def captcha_validate(key, value):
    try:
        captcha = CaptchaStore.objects.get(response=value, hashkey=key, expiration__gt=get_safe_now())
    except CaptchaStore.DoesNotExist:
        return False
    else:
        captcha.delete()
        return True