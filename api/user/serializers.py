from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import authentication_classes, permission_classes
from .models import CustomUser



class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validate_date):
        password = validate_date.pop('password', None)
        instance = self.Meta.model(**validate_date)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validate_date):
        for attr, value in validate_date.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


    class Meta:
        model = CustomUser
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('name', 'email', 'password', 'phone', 'gender', 'is_active', 'is_staff', 'is_superuser')