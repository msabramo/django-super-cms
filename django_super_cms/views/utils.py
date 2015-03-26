# -*- coding:utf-8 -*-
# PROJECT_NAME : mysite
# FILE_NAME    : 
# AUTHOR       : younger shen
from captcha.models import CaptchaStore
from captcha.models import get_safe_now
from django.http import Http404, JsonResponse
from django.views.decorators.http import require_safe


@require_safe
def captchat_verify_view(request):
    if len(request.GET.keys()) == 1 and len(request.GET.values()) == 1:
        captcha_key = request.GET.keys()[0]
        captcha_value = request.GET.values()[0]
        try:
            CaptchaStore.objects.get(response=captcha_value, hashkey=captcha_key, expiration__gt=get_safe_now())
        except CaptchaStore.DoesNotExist:
            raise Http404
        else:
            return JsonResponse({'state': True})
    else:
        raise Http404