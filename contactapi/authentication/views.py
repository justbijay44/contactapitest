from django.shortcuts import render

from .serializers import UserSerializer,LoginSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterView(GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CustomTokenPairSerializers(TokenObtainPairSerializer):

    serializer_class = LoginSerializer


    def validate(self, attrs):
        data = super().validate(attrs)
        data = {
            'username' : self.user.username,
            'access': data['access'],
            'refresh' : data['refresh'],
        }
        return data

class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializers