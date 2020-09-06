from django.db import models


# Create your models here.
class Dish(models.Model):

    # Dish types declaration
    STARTER = 'starter'
    MAIN = 'main'
    DESERT = 'desert'
    DAILY_SPECIAL = 'special'
    DISH_TYPES = (
        (STARTER, 'Appetizing starter'),
        (MAIN, 'Main course'),
        (DESERT, 'Delicious desert'),
        (DAILY_SPECIAL, 'Daily special')
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

    title = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField()
    type = models.CharField(choices=DISH_TYPES, max_length=10)
    day = models.CharField(choices=DAYS, max_length=2, default=EVERYDAY)
    serving_time = models.CharField(choices=SERVING_TIMES, max_length=10, default=LUNCH_AND_DINNER)
    # TODO: Add image support

    class Meta:
        ordering = ['type']