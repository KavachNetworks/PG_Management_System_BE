from django.shortcuts import render
from . serializers import LoginSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from .models import AdminUser

# Create your views here.


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        userId = request.user.id
        username = request.user.username
        enterpriseId = AdminUser.objects.filter(adminId=username).values('enterpriseId')
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key,"userId":userId,"username":username,"enterpriseId":enterpriseId}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication, )

    def post(self, request):
        logout(request)
        return Response(status=204)

# this is user defined method
# perform makemigrations
# perform migrate
# login
# api --->  http://localhost:8080/auth/login/
# logout
# api --->  http://localhost:8080/auth/logout/
# for using default method----
# type  in cmd- pip install djoser
# api ----> http://localhost:8080/auth/token/login/
# api ----> http://localhost:8080/auth/token/logout/