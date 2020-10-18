from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.response import Response

from api.models import Dish, DeliveryOrder, DeliveryOrderItem, TableBooking, EventPreBooking, CookingLessonBooking
from api.permissions import BookingPermission, IsAdminUserOrReadOnly
from api.serializers import DishSerializer, UserSerializer, DeliveryOrderSerializer, \
    DeliveryOrderItemSerializer, TableBookingSerializer, EventPreBookingSerializer, CookingLessonBookingSerializer
from rest_framework.decorators import action
from django.db.models import Q


class BookingMixin:
    """Mixin used by all booking view. It ensure the user is passed to the model if available at creation time.
    For non administrators, the query set is restricted to the elements owned by the user while administrators
    have access to all bookings."""
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

    # List of extra route to get all the started, mains, desert, side, lunch or dinner daily specials.
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
    Viewset of users object.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeliveryOrderViewSet(BookingMixin, viewsets.ModelViewSet):
    """
    Viewset for deliver orders
    """
    queryset = DeliveryOrder.objects.all()
    serializer_class = DeliveryOrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'time']
    ordering = ['date', 'time']


class DeliveryOrderItemViewSet(viewsets.ModelViewSet):
    """
    Viewset of delivery order items.
    """
    queryset = DeliveryOrderItem.objects.all()
    serializer_class = DeliveryOrderItemSerializer


class TableBookingViewSet(BookingMixin, viewsets.ModelViewSet):
    """
    Viewset of table booking.
    """
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'time']
    ordering = ['date', 'time']


class EventPreBookingViewSet(BookingMixin, viewsets.ModelViewSet):
    """
    Viewset of event pre booking.
    """
    queryset = EventPreBooking.objects.all()
    serializer_class = EventPreBookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'time']
    ordering = ['date', 'time']


class CookingLessonBookingViewSet(BookingMixin, viewsets.ModelViewSet):
    """
    Cooking lesson booking.
    """
    queryset = CookingLessonBooking.objects.all()
    serializer_class = CookingLessonBookingSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'time']
    ordering = ['date', 'time']


