from django.contrib.auth.models import User
from rest_framework import serializers


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    """
    Custom serialization class for django-rest-registration.
    It ensures the fields first_name, last_name and email are present when
    a registration is submitted.
    """
    email = serializers.EmailField(allow_blank=False, allow_null=False)
    first_name = serializers.CharField(allow_blank=False, allow_null=False)
    last_name = serializers.CharField(allow_blank=False, allow_null=False)
    password = serializers.CharField(allow_blank=False, allow_null=False)
    password_confirm = serializers.CharField(allow_blank=False, allow_null=False)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password', 'password_confirm', 'first_name', 'last_name']

    def validate(self, attrs):
        # Check that password is equals to password_confirm
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("The password and its confirmation doesn't match")

        return attrs

    def create(self, validated_data):
        # password_confirm is not expected by a User object. Remove it before
        # object creation.
        data = validated_data.copy()
        del data['password_confirm']
        obj = super().create(data)
        # Update the password using the set_password method, it ensure the
        # password is hashed.
        obj.set_password(data['password'])
        obj.save()
        return obj


class UserRegistrationOutputSerializer(serializers.HyperlinkedModelSerializer):
    """
    Override of the serializer that outputs the registration data.
    """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'first_name', 'last_name']

