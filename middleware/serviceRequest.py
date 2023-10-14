import uuid
from builtins import print

from django.conf import settings
from django.contrib import auth
from django.http import HttpResponseForbidden
from django.contrib.sessions.models import Session


class Operation:

    @classmethod
    def _setHeader(cls, request, headersInfo):
        if len(headersInfo) <= 0: request.__dict__.pop('headers', None); return
        headersName = list(headersInfo.keys())[0]
        request.META[headersName] = headersInfo.pop(headersName)
        return cls._setHeader(request, headersInfo)


class ServiceMiddleware:

    def __init__(self, getResponse):
        self.getResponse = getResponse

    def __call__(self, request):
        requestID = str(uuid.uuid4())
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[-1].strip() if x_forwarded_for else request.META.get('REMOTE_ADDR')
        Operation._setHeader(request, {'REQUEST_ID': requestID})
        settings.BACKEND_LOGGER.info(f"{'~'*30} New Request({request.META.get('REQUEST_ID')}) Started {'~'*30}")
        settings.BACKEND_LOGGER.info(f"Request({request.META.get('REQUEST_ID')}) - Requester IP: {request.META.get('REMOTE_ADDR')}")
        settings.BACKEND_LOGGER.info(f"Request({request.META.get('REQUEST_ID')}) - Request To: {request.method} {request.scheme}://{request.get_host()}{request.path}")
        response = self.getResponse(request)
        settings.BACKEND_LOGGER.info(f"{'-'*30} Request({request.META.get('REQUEST_ID')}) End {'-'*30}")
        return response


