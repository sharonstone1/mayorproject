from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import Dish, DeliveryOrder, DeliveryOrderItem


class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ['url', 'id', 'title', 'price', 'description', 'type', 'day', 'serving_time']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'first_name', 'last_name', 'email', 'password']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name', 'permissions']


class DeliveryOrderItemSerializer(serializers.HyperlinkedModelSerializer):
    # dish = serializers.ReadOnlyField(source='dish.title')
    # order = serializers.HyperlinkedIdentityField(many=True, view_name='deliveryorder-detail', read_only=True)

    class Meta:
        model = DeliveryOrderItem
        fields = ['url', 'id', 'dish', 'count']


class DeliveryOrderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    items = DeliveryOrderItemSerializer(many=True)

    class Meta:
        model = DeliveryOrder
        fields = ['url', 'id', 'date', 'time', 'user', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = DeliveryOrder.objects.create(**validated_data)
        for item_data in items_data:
            DeliveryOrderItem.objects.create(order=order, **item_data)
        return order


# serializer = DeliveryOrderSerializer(data={'date': '2020-09-09', 'time': '23:21', 'items': [{'dish': 2, 'count': 10 }]})