from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

import rest_registration.api.views.login as framework_login


@csrf_protect
def login(request, *args, **kwargs):
    """
    This function ensures that login is protected by csrf.
    The request is forwarded to rest-framework-registration login
    """
    return framework_login(request, *args, **kwargs)
