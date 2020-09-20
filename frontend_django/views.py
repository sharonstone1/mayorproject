from django.conf import settings
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.views.generic.base import TemplateView


from django.contrib.auth import authenticate, login, logout


class IndexTemplateView(TemplateView):
    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        return super().get(request, args, kwargs)

    def get_template_names(self):
        template_name = "index.html"
        return template_name