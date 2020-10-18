import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


def dish_image_name(instance, filename):
    """Create a unique name for the image associated to a dish"""
    extension = filename.split(".")[-1]
    name = f"dishes/images/{uuid.uuid4()}.{extension}"
    return name


# Create your models here.
class Dish(models.Model):
    """Model for the dishes served in the restaurant"""
    # Dish types declaration
    STARTER = 'starter'
    MAIN = 'main'
    DESSERT = 'dessert'
    DAILY_SPECIAL = 'special'
    SIDE = 'side'
    DISH_TYPES = (
        (STARTER, 'Appetizing starter'),
        (MAIN, 'Main course'),
        (DESSERT, 'Delicious dessert'),
        (DAILY_SPECIAL, 'Daily special'),
        (SIDE, 'Sides')
    )

    # Days declaration
    MONDAY = 'MO'
    TUESDAY = 'TU'
    WEDNESDAY = 'WE'
    THURSDAY = 'TH'
    FRIDAY = 'FR'
    SATURDAY = 'SA'
    SUNDAY = 'SU'
    EVERYDAY = '*'
    DAYS = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
        (EVERYDAY, 'Everyday'),
    )

    # Serving time choices
    LUNCH = 'lunch'
    DINNER = 'dinner'
    LUNCH_AND_DINNER = '*'
    SERVING_TIMES = (
        (LUNCH, 'Lunch'),
        (DINNER, 'Dinner'),
        (LUNCH_AND_DINNER, 'Lunch and Dinner')
    )

    # Fields of the model
    title = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField(blank=True)
    type = models.CharField(choices=DISH_TYPES, max_length=10)
    day = models.CharField(choices=DAYS, max_length=2, default=EVERYDAY)
    serving_time = models.CharField(choices=SERVING_TIMES, max_length=10, default=LUNCH_AND_DINNER)
    image = models.ImageField(upload_to=dish_image_name, null=True, blank=True)

    class Meta:
        ordering = ['type']


class DeliveryOrder(models.Model):
    """Model for a delivery order"""
    # The fields fullname and email are mandatory if the owner field is null.
    # This allow an unregistered user to pass a delivery order
    fullname = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='delivery_orders', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()


class DeliveryOrderItem(models.Model):
    """Item associated to a delivery order"""
    # The model references the Dish and the order as foreign keys.
    dish = models.ForeignKey('Dish', on_delete=models.CASCADE)
    count = models.PositiveSmallIntegerField()
    order = models.ForeignKey('DeliveryOrder', related_name='items', on_delete=models.CASCADE)


class TableBooking(models.Model):
    """Model for a delivery order"""
    # The fields fullname and email are mandatory if the owner field is null.
    # This allow an unregistered user to pass a delivery order
    fullname = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='table_bookings', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = PhoneNumberField()
    date = models.DateField()
    time = models.TimeField()
    guest_count = models.PositiveSmallIntegerField()
    vip = models.BooleanField()


class CookingLessonBooking(models.Model):
    """Model for a delivery order"""

    # Constants defining the type of lesson
    ONLINE = 'stream'
    IN_PERSON = 'live'
    LESSON_TYPE = (
        (ONLINE, 'Cooking lesson live streaming'),
        (IN_PERSON, 'At the restaurant'),
    )

    # Session time
    MORNING = 'morning'
    AFTERNOON = 'afternoon'
    LESSON_TIME = (
        (MORNING, 'Starting at 8 o\'clock until lunch'),
        (AFTERNOON, 'Starting at 15 o\'clock until dinner'),
    )

    # The fields fullname and email are mandatory if the owner field is null.
    # This allow an unregistered user to pass a delivery order
    fullname = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='cooking_lessons', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=500)
    date = models.DateField()
    type = models.CharField(choices=LESSON_TYPE, max_length=10)
    time = models.CharField(choices=LESSON_TIME, max_length=10)


class EventPreBooking(models.Model):
    """Model for an event pre booking"""
    # The fields fullname and email are mandatory if the owener field is null.
    # This allow an unregistered user to pass a delivery order
    fullname = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    owner = models.ForeignKey('auth.User', related_name='events', on_delete=models.CASCADE, blank=True, null=True)
    phone_number = PhoneNumberField()
    address = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
