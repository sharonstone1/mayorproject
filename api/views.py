from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, permissions, filters
from rest_framework import views
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Dish, DeliveryOrder, DeliveryOrderItem, TableBooking, EventPreBooking, CookingLessonBooking
from api.permissions import BookingPermission, IsAdminUserOrReadOnly
from api.serializers import DishSerializer, UserSerializer, DeliveryOrderSerializer, \
    DeliveryOrderItemSerializer, TableBookingSerializer, EventPreBookingSerializer, CookingLessonBookingSerializer, \
    LoginSerializer
from rest_framework.decorators import action, api_view
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout


class BookingMixin:
    permission_classes = [BookingPermission]

    def perform_create(self, serializer):
        # Pass the user to the serializer if it isn't anonymous
        owner = None if self.request.user.is_anonymous else self.request.user
        serializer.save(owner=owner)

    def get_queryset(self):
        """
        Filter for the user if it is not staff
        """
        user = self.request.user
        if user.is_staff:
            return self.queryset
        return self.queryset.filter(owner=user)



class Login(APIView):
    permission_classes = (permissions.AllowAny,)

    @method_decorator(csrf_protect)
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Extract the username and password
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        # Try to authenticate the user
        user = authenticate(username=username, password=password)
        if user is not None:
            # the password verified for the user
            if user.is_active:
                login(request._request, user)
                return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_401_UNAUTHORIZED)



class Logout(APIView):
    def post(self, request, format=None):
        logout(request._request)
        return Response(status=status.HTTP_401_UNAUTHORIZED)


# Create your views here.
class DishViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [IsAdminUserOrReadOnly]

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


class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeliveryOrderViewSet(BookingMixin, viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'time']
    ordering = ['date', 'time']


class DeliveryOrderItemViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = DeliveryOrderItem.objects.all()
    serializer_class = DeliveryOrderItemSerializer


class TableBookingViewSet(BookingMixin, viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'time']
    ordering = ['date', 'time']


class EventPreBookingViewSet(BookingMixin, viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = EventPreBooking.objects.all()
    serializer_class = EventPreBookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'time']
    ordering = ['date', 'time']


class CookingLessonBookingViewSet(BookingMixin, viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = CookingLessonBooking.objects.all()
    serializer_class = CookingLessonBookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'time']
    ordering = ['date', 'time']


