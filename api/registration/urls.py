from django.urls import path, include
from api.registration.views import login

# Hack the rest-framework-registration urls, there is no CSRF protection for the login!
# We replace the login route to a proxy that ensure CSRF validation.
rest_registration_urls = include('rest_registration.api.urls')
rest_registration_urls[0].urlpatterns = [up for up in rest_registration_urls[0].urlpatterns if not up.name == 'login']
rest_registration_urls[0].urlpatterns.append(path('login/', login))

urlpatterns = [
    path('', rest_registration_urls)
]
