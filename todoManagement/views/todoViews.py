import json, datetime
from rest_framework.views import APIView
from rest_framework import status as rs
from rest_framework.response import Response
from todoManagement.models import *
from todoManagement.serializers import todoTaskListSerializer

from django.conf import settings
from utilities import *


class todoManager(APIView):
    def get(self, request):
        user = request.META['user_id']

        settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Get All Todo List > Start {'=' * 30}")
        try:
            todo_list = dataSerializer(todoTaskList.objects.filter(user_id=user))
            settings.BACKEND_LOGGER.info(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: All Todo List Send Successfully")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Get All Todo List > End {'=' * 30}")
            return makeJsonResponse(todo_list, '', rs.HTTP_200_OK)
        except Exception as e:
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Something Went Wrong! Please Try Again; Exception : {str(e)}; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Get All Todo List > End {'=' * 30}")
            return makeJsonResponse('', "Something Went Wrong! Please Try Again", rs.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self, request):
        settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create Todo Task > Start {'=' * 30}")
        data = {}
        data['name'] = request.data.get('name', '')
        data['description'] = request.data.get('description', '')
        data['deadline'] = request.data.get('deadline', '')
        data['user'] = request.META['user_id']

        if not (data['name'] and data['description'] and data['deadline'] and data['user']):
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Invalid Request! Please Provide the details carefully; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create Todo Task > End {'=' * 30}")
            return makeJsonResponse('', 'Invalid Request! Please Provide the details carefully', rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            data['deadline'] = datetime.datetime.strptime(data['deadline'], '%Y-%m-%d %H:%M:%S')
        except:
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Invalid Request!Please Enter a valid deadline; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create Todo Task > End {'=' * 30}")
            return makeJsonResponse('', 'Invalid Request! Please Enter a valid deadline', rs.HTTP_406_NOT_ACCEPTABLE)
        try:
            serializer = todoTaskListSerializer(data=data)
            serializer_valid = serializer.is_valid()
            if not serializer_valid:
                settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Invalid Request! Please Provide the details carefully; request body : {json.dumps(request.data)}")
                settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create Todo Task > End {'=' * 30}")
                return makeJsonResponse('', "Invalid Request! Please Provide the details carefully", rs.HTTP_406_NOT_ACCEPTABLE)
            serializer.save()
            settings.BACKEND_LOGGER.info(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Todo List Created Successfully!; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create Todo Task > End {'=' * 30}")
            return makeJsonResponse("Todo Task Created Successfully!", '', rs.HTTP_201_CREATED)

        except Exception as e:
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Something Went Wrong! Please Try Again; Exception : {str(e)}; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Create Todo Task > End {'=' * 30}")
            return makeJsonResponse('', "Something Went Wrong! Please Try Again", rs.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Update Todo Task > Start {'=' * 30}")
        data = {}
        data['id'] = request.data.get('todo_id', '')
        if request.data.get('name', ''): data['name'] = request.data.get('name', '')
        if request.data.get('description', ''): data['description'] = request.data.get('description', '')
        deadline = request.data.get('deadline', '')
        user = request.META['user_id']

        if not ((request.data.get('name', '') or request.data.get('description', '') or request.data.get('deadline', '')) and data['id']):
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Invalid Request! Please Provide the details carefully; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Update Todo Task > End {'=' * 30}")
            return makeJsonResponse('', 'Invalid Request! Please Provide the details carefully', rs.HTTP_406_NOT_ACCEPTABLE)

        if deadline:
            try:
                data['deadline'] = datetime.datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')
            except:
                settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Invalid Request!Please Enter a valid deadline; request body : {json.dumps(request.data)}")
                settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Update Todo Task > End {'=' * 30}")
                return makeJsonResponse('', 'Invalid Request! Please Enter a valid deadline', rs.HTTP_406_NOT_ACCEPTABLE)

        try:
            todo_task = todoTaskList.objects.filter(id=data['id'], user_id=user)
            if todo_task:
                data['updatedAt'] = datetime.datetime.now()
                todo_task.update(**data)
                settings.BACKEND_LOGGER.info(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Todo List Created Successfully!; request body : {json.dumps(request.data)}")
                settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Update Todo Task > End {'=' * 30}")
                return makeJsonResponse("Todo Task Update Successfully!", '', rs.HTTP_200_OK)
            else:
                settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Todo Task does not exist.; Exception : {str(e)}; request body : {json.dumps(request.data)}")
                settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Update Todo Task > End {'=' * 30}")
                return makeJsonResponse('', "Todo Task does not exist.", rs.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Something Went Wrong! Please Try Again; Exception : {str(e)}; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Update Todo Task > End {'=' * 30}")
            return makeJsonResponse('', "Something Went Wrong! Please Try Again", rs.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Delete Todo Task > Start {'=' * 30}")
        data = {}
        data['id'] = request.data.get('todo_id', '')
        user = request.META['user_id']

        if not (data['id'] and user):
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Invalid Request! Please Provide the details carefully; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Delete Todo Task > End {'=' * 30}")
            return makeJsonResponse('', 'Invalid Request! Please Provide the details carefully', rs.HTTP_406_NOT_ACCEPTABLE)

        try:
            todo_task = todoTaskList.objects.filter(id=data['id'], user_id=user)
            if todo_task:
                todo_task.delete()
                settings.BACKEND_LOGGER.info(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Todo List Created Successfully!; request body : {json.dumps(request.data)}")
                settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Delete Todo Task > End {'=' * 30}")
                return makeJsonResponse("Todo Task Deleted Successfully!", '', rs.HTTP_200_OK)
            else:
                settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Todo Task does not exist.; request body : {json.dumps(request.data)}")
                settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Delete Todo Task > End {'=' * 30}")
                return makeJsonResponse('', "Todo Task does not exist.", rs.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            settings.BACKEND_LOGGER.error(f"Request_id: {request.META.get('REQUEST_ID')} {'=' * 5}; message: Something Went Wrong! Please Try Again; Exception : {str(e)}; request body : {json.dumps(request.data)}")
            settings.BACKEND_LOGGER.info(f"{'=' * 30} {request.META.get('REQUEST_ID')} - Delete Todo Task > End {'=' * 30}")
            return makeJsonResponse('', "Something Went Wrong! Please Try Again", rs.HTTP_500_INTERNAL_SERVER_ERROR)