from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response

from api.models import Dish, DeliveryOrder, DeliveryOrderItem, TableBooking, EventPreBooking
from api.serializers import DishSerializer, UserSerializer, GroupSerializer, DeliveryOrderSerializer, \
    DeliveryOrderItemSerializer, TableBookingSerializer, EventPreBookingSerializer
from rest_framework.decorators import action
from django.db.models import Q

# Create your views here.
class DishViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    def get_dish_category(self, dish_type, serving_time, request, *args, **kwargs):
        starters = Dish.objects.filter(Q(type=dish_type) & Q(serving_time=serving_time))

        page = self.paginate_queryset(starters)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(starters, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def starters(self, request, *args, **kwargs):
        return self.get_dish_category(Dish.STARTER, Dish.LUNCH_AND_DINNER, request, args, kwargs)

    @action(detail=False)
    def mains(self, request, *args, **kwargs):
        return self.get_dish_category(Dish.MAIN, Dish.LUNCH_AND_DINNER, request, args, kwargs)

    @action(detail=False)
    def deserts(self, request, *args, **kwargs):
        return self.get_dish_category(Dish.DESSERT, Dish.LUNCH_AND_DINNER, request, args, kwargs)

    @action(detail=False)
    def lunch_daily_specials(self, request, *args, **kwargs):
        return self.get_dish_category(Dish.DAILY_SPECIAL, Dish.LUNCH, request, args, kwargs)

    @action(detail=False)
    def dinner_daily_specials(self, request, *args, **kwargs):
        return self.get_dish_category(Dish.DAILY_SPECIAL, Dish.DINNER, request, args, kwargs)

    @action(detail=False)
    def sides(self, request, *args, **kwargs):
        return self.get_dish_category(Dish.SIDE, Dish.LUNCH_AND_DINNER, request, args, kwargs)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DeliveryOrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer


class DeliveryOrderItemViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = DeliveryOrderItem.objects.all()
    serializer_class = DeliveryOrderItemSerializer


class TableBookingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer


class EventPreBookingViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = EventPreBooking.objects.all()
    serializer_class = EventPreBookingSerializer

