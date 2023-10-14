from rest_framework import authentication
from rest_framework import exceptions
from django.contrib import auth
from rest_framework_simplejwt import authentication as jwtRestAuth
from django.conf import settings


class todoAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        authobj = jwtRestAuth.JWTAuthentication()
        authData = authobj.authenticate(request)
        if authData:
            request.META['user_id'] = authData[0].id
            settings.BACKEND_LOGGER.info(f"Request({request.META.get('REQUEST_ID')}) - Requester : {authData[0].email}")
        else:
            settings.BACKEND_LOGGER.info(f"Request({request.META.get('REQUEST_ID')}) - Requester : {auth.models.AnonymousUser()}")

        return authData