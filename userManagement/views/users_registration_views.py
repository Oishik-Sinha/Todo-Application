import json
from rest_framework.views import APIView
from rest_framework import status as rs
from django.contrib.auth.models import User

from django.conf import settings
from utilities import *


class userRegistration(APIView):
    permission_classes = ()

    def post(self, request):
        settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create User > Start {'=' * 30}")
        data = {}
        data['password'] = request.data.get('password', '')
        confirm_password = request.data.get('confirm_password', '')
        data['username'] = request.data.get('username', '')
        data['first_name'] = request.data.get('first_name', '')
        data['last_name'] = request.data.get('last_name', '')
        data['email'] = request.data.get('email', '')

        if not (data['password'] == confirm_password):
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Invalid Request! Password and Confirm Password must be same.; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create User > End {'=' * 30}")
            return makeJsonResponse('', 'Invalid Request! Password and Confirm Password must be same.', rs.HTTP_406_NOT_ACCEPTABLE)

        if not (data['username'] and data['first_name'] and data['last_name'] and data['email'] and data['password']):
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Invalid Request! Please Provide the details carefully; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create User > End {'=' * 30}")
            return makeJsonResponse('', 'Invalid Request! Please Provide the details carefully', rs.HTTP_406_NOT_ACCEPTABLE)

        try:
            if User.objects.filter(email=data['email']) or User.objects.filter(username=data['username']):
                settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: User Already Exist; request body : {json.dumps(request.data)}")
                settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create User > End {'=' * 30}")
                return makeJsonResponse('', 'User Already Exist', rs.HTTP_406_NOT_ACCEPTABLE)
            user = User.objects.create_user(**data)
            
            settings.BACKEND_LOGGER.info(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: User Has Been Created Successfully.; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create User > End {'=' * 30}")
            return makeJsonResponse('You have registered successfully. Please Login!', '', rs.HTTP_201_CREATED)
            
        except Exception as e:
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Something Went Wrong! Please Try Again; Exception : {str(e)}; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create User > End {'=' * 30}")
            return makeJsonResponse('', "Something Went Wrong! Please Try Again", rs.HTTP_500_INTERNAL_SERVER_ERROR)
