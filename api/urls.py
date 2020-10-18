from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'dishes', views.DishViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'orders', views.DeliveryOrderViewSet)
router.register(r'orders-items', views.DeliveryOrderItemViewSet)
router.register(r'table-booking', views.TableBookingViewSet)
router.register(r'event-pre-booking', views.EventPreBookingViewSet)
router.register(r'cooking-lessons', views.CookingLessonBookingViewSet)

# # The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path(r'auth/', include('api.registration.urls')), # Authentication provided by rest_register goes into /auth/
]