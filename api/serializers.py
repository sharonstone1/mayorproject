from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Dish, DeliveryOrder, DeliveryOrderItem, TableBooking, EventPreBooking, CookingLessonBooking
import datetime


class ReadWriteSerializerMethodField(serializers.Field):
    """
    Serializer that intercepts serialization and deserialization of a field.
    The serializer using this field must provides the methods:
       - get_{field_name}: to return the representation
       - set_{field_name}: to set the internal value
    """

    def __init__(self, **kwargs):
        kwargs['source'] = '*'
        self.deserializer_field = kwargs.pop('deserializer_field')
        self.get_method_name = None
        self.set_method_name = None
        super(ReadWriteSerializerMethodField, self).__init__(**kwargs)

    def bind(self, field_name, parent):
        self.field_name = field_name
        self.get_method_name = f'get_{field_name}'
        self.set_method_name = f'set_{field_name}'
        super(ReadWriteSerializerMethodField, self).bind(field_name, parent)

    def to_representation(self, value):
        method = getattr(self.parent, self.get_method_name)
        return method(value)

    def to_internal_value(self, data):
        value = self.deserializer_field.to_internal_value(data)
        method = getattr(self.parent, self.set_method_name)
        return {self.field_name: method(value)}


class BookingSerializerMixin:
    """
    Mixin that correctly serialize the fullname for Booking elements:
    Any type of booking can be made by an anonymous but in such case, the fields
    username and email must be filled. If it is not the case then an error is raised.
    Similarly, if the booking has been made by a registered users, the email and fullname
    value serialized are the one in the user object.
    """
    # Email setter and getter
    def get_email(self, obj):
        if obj.owner:
            return obj.owner.email
        return obj.email

    def set_email(self, value):
        return value

    # Fullname setter and getter
    def get_fullname(self, obj):
        if obj.owner:
            return f'{obj.owner.first_name} {obj.owner.last_name}'
        return obj.fullname

    def set_fullname(self, value):
        return value

    def validate(self, data):
        """
        Validation of fullname and email. This method must be called by derived class if overridden
        """
        request = self.context.get('request', None)
        if request:
            user = request.user

        if not data['fullname'] or data['fullname'] == '' or not data['email'] or data['email'] == '':
            if not user or user.is_anonymous:
                raise serializers.ValidationError(
                    "Booking a table must be associated to a fullname and email or a registered user.")
        return data


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ['url', 'title', 'price', 'description', 'type', 'day', 'serving_time', 'image']


class DeliveryOrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryOrderItem
        fields = ['url', 'dish', 'count', 'order']


class DeliveryOrderItemCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeliveryOrderItem
        fields = ['url', 'dish', 'count']

class DeliveryOrderSerializer(BookingSerializerMixin, serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    fullname = ReadWriteSerializerMethodField(deserializer_field=serializers.CharField())
    email = ReadWriteSerializerMethodField(deserializer_field=serializers.CharField())
    items = DeliveryOrderItemCreateSerializer(many=True)

    class Meta:
        model = DeliveryOrder
        fields = ['url', 'owner', 'fullname', 'email', 'address', 'phone_number', 'date', 'time', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = DeliveryOrder.objects.create(**validated_data)
        for item_data in items_data:
            DeliveryOrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        # Remove items from the original order
        for item in instance.items.all():
            item.delete()

        # Update with new ones
        items_data = validated_data.pop('items')
        for item_data in items_data:
            DeliveryOrderItem.objects.create(order=instance, **item_data)
        return super().update(instance, validated_data)


    def validate(self, data):
        # Validation of the date and time
        if data['date'] == datetime.date.today():
            limit = datetime.datetime.now() + datetime.timedelta(hours=1)
            time_limit = limit.time()

            if data['time'] < time_limit:
                raise serializers.ValidationError(
                    "Same day reservations must be made one hours early")

        for item in data['items']:
            dish = item['dish']
            if dish.type == Dish.DAILY_SPECIAL:
                # Check the day
                day = data['date'].weekday()
                dish_day = Dish.DAYS[day]
                if dish.day != dish_day[0]:
                    raise serializers.ValidationError("One of the item cannot be ordered for the day selected")

                if dish.serving_time == Dish.DINNER and data['time'] < datetime.time(19):
                    raise serializers.ValidationError("One of the item must be ordered between 19:00 and 23:59")

                if dish.serving_time == Dish.LUNCH and data['time'] > datetime.time(16):
                    raise serializers.ValidationError("One of the item cannot must be ordered between 12:00 and 16:00")

        return super().validate(data)

    def validate_time(self, value):
        if not datetime.time(12) <= value <= datetime.time(16) and not datetime.time(19) <= value <= datetime.time(23, 59):
            raise serializers.ValidationError("Time of booking is between 12:00 to 16:00 and 19:00 to 23:59 pm")
        return value

    def validate_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("Date must not be in the past")
        return value

    def validate_items(self, value):
        if not value:
            raise serializers.ValidationError("Please provide the items of the order")
        return value


class TableBookingSerializer(BookingSerializerMixin, serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    fullname = ReadWriteSerializerMethodField(deserializer_field=serializers.CharField())
    email = ReadWriteSerializerMethodField(deserializer_field=serializers.CharField())

    class Meta:
        model = TableBooking
        fields = ['url', 'owner', 'fullname', 'email', 'phone_number', 'date', 'time', 'guest_count', 'vip']

    def validate(self, data):
        # Validation of the date and time
        if data['date'] == datetime.date.today():
            limit = datetime.datetime.now() + datetime.timedelta(hours=2)
            time_limit = limit.time()

            if data['time'] < time_limit:
                raise serializers.ValidationError(
                    "Same day reservations must be made two hours early")

        return super().validate(data)

    def validate_guest_count(self, value):
        if not 1 <= value <= 10:
            raise serializers.ValidationError("Guests must be between 1 and 10")
        return value

    def validate_time(self, value):
        if not datetime.time(12) <= value <= datetime.time(23):
            raise serializers.ValidationError("Time of booking is between 12 to 23 pm")
        return value

    def validate_date(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("Date must not be in the past")
        return value


class EventPreBookingSerializer(BookingSerializerMixin, serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    fullname = ReadWriteSerializerMethodField(deserializer_field=serializers.CharField())
    email = ReadWriteSerializerMethodField(deserializer_field=serializers.CharField())

    class Meta:
        model = EventPreBooking
        fields = ['url', 'owner', 'fullname', 'email', 'phone_number', 'date', 'time', 'address']

    def validate_time(self, value):
        if not datetime.time(14) <= value <= datetime.time(18):
            raise serializers.ValidationError("Time of booking is between 14 to 18")
        return value

    def validate_date(self, value):
        if value < (datetime.date.today() + datetime.timedelta(days=14)):
            raise serializers.ValidationError("Events must be booked 14 days in advance")
        if value.weekday() < 4:
            raise serializers.ValidationError("Date must be a Friday, Saturday or Sunday")
        return value



class CookingLessonBookingSerializer(BookingSerializerMixin, serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='user-detail')
    fullname = ReadWriteSerializerMethodField(deserializer_field=serializers.CharField())
    email = ReadWriteSerializerMethodField(deserializer_field=serializers.CharField())

    class Meta:
        model = CookingLessonBooking
        fields = ['url', 'owner', 'fullname', 'email', 'phone_number', 'address', 'date', 'time', 'type']

    def validate_date(self, value):
        if value < (datetime.date.today() + datetime.timedelta(days=3)):
            raise serializers.ValidationError("Cooking lesson orders must be set 3 days in advance")
        return value



class UserSerializer(serializers.HyperlinkedModelSerializer):
    # delivery_orders = serializers.ReadOnlyField()
    table_bookings = TableBookingSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'email', 'table_bookings']


class ProfileUserSerializer(serializers.HyperlinkedModelSerializer):
    table_bookings = TableBookingSerializer(many=True, read_only=True)
    delivery_orders = DeliveryOrderSerializer(many=True, read_only=True)
    cooking_lessons = CookingLessonBookingSerializer(many=True, read_only=True)
    events = EventPreBookingSerializer(many=True, read_only=True)
    is_staff = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['url', 'username', 'first_name', 'last_name', 'email', 'is_staff',
                  'table_bookings',
                  'delivery_orders',
                  'cooking_lessons',
                  'events'
        ]



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
