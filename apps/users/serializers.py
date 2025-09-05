from rest_framework import serializers
from apps.users.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone', 'name']
        read_only_fields = ['id']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,min_length=6)

    class Meta:
        model = User
        fields = ['id', 'phone', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        user = User.objects.create(
            phone=validated_data['phone'],
            password=validated_data['password'],
            name=validated_data.get('name', '')
        )
        return user

class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)
    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')
       
        if phone and password:
            user = authenticate(phone=phone, password=password)
            if not user:
                raise serializers.ValidationError("Неверный телефон или пароль")
        else:
            raise serializers.ValidationError("Необходимо указать номер телефона и пароль")

        attrs['user'] = user
        return attrs