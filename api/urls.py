from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'dishes', views.DishViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'orders', views.DeliveryOrderViewSet)
router.register(r'orders-items', views.DeliveryOrderItemViewSet)

# # The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]