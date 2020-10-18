from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView


class IndexTemplateView(TemplateView):
    """View of the index"""

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        """Forward to parent get method. The decorator ensure the csrf cookie is present in the response."""
        return super().get(request, args, kwargs)

    def get_template_names(self):
        """The template is index.html in the template folder"""
        template_name = "index.html"
        return template_name
