from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from django.contrib.auth.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta: 
        model = User
        fields = ('id','username', 'email', 'password')
    
    def create(self, validated_data):
        validated_data ['password'] = make_password(validated_data['password'])
        # return super().create(validated_data)
        return User.objects.create(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta: 
        model = User
        fields = ('username', 'password')
    

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = ('id','username', 'email')
