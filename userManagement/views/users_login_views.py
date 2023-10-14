
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status as rs
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
import datetime
from utilities import *
from django.conf import settings

class login(APIView):
    permission_classes = ()
    def post(self, request):
        settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Login User > Start {'=' * 30}")

        data = {}
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        settings.BACKEND_LOGGER.info(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Login Request For user {username}")
        if username and password:
            try:
                user = User.objects.filter(username=username)
                if user:
                    valid_user = check_password(password, user[0].password)
                    if valid_user:
                        refresh = RefreshToken.for_user(user.first())
                        user.update(**{"last_login":datetime.datetime.now()})
                        settings.BACKEND_LOGGER.info(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: User Tokens and details are successfully send")
                        settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Login User > End {'=' * 30}")
                        return makeJsonResponse({'refreshToken': str(refresh),'accessToken': str(refresh.access_token)}, '', rs.HTTP_200_OK)
                    else:
                        settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: User Does not exist; request body : {json.dumps(request.data)}")
                        settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Login User > End {'=' * 30}")
                        return makeJsonResponse({'refreshToken': '','accessToken': ''}, "User does not exist. Please Register First!", rs.HTTP_401_UNAUTHORIZED)
                else:
                    settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: User Credential Invalid; request body : {json.dumps(request.data)}")
                    settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Login User > End {'=' * 30}")
                    return makeJsonResponse({'refreshToken': '', 'accessToken': ''}, "User Credential Invalid. Please Enter a valid User Credentials", rs.HTTP_401_UNAUTHORIZED)
            except Exception as e:
                settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Something Went Wrong! Please Try Again; Exception : {str(e)}; request body : {json.dumps(request.data)}")
                settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Login User > End {'=' * 30}")
                return makeJsonResponse({'refreshToken': '','accessToken': ''}, "Internal Server Error", rs.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: User Credential Key missing; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Login User > End {'=' * 30}")
            return makeJsonResponse({'refreshToken': '', 'accessToken': ''}, "Please Enter a valid User Credentials", rs.HTTP_403_FORBIDDEN)

