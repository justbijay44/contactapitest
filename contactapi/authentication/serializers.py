from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(max_length = 150)
    last_name = serializers.CharField(max_length = 150)
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 100, min_length = 8, write_only = True)

    class Meta:
        model = User
        fields = ['username','email','first_name', 'last_name', 'password']

    def validate(self, attrs):

        email = attrs.get('email', '')

        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'email' : 'Email already exists'})
        return super().validate(attrs)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(max_length = 100, min_length = 8, write_only = True)

    class Meta:
        model = User
        fields = ['username', 'password']

