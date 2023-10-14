from rest_framework import serializers

from .models import *


class todoTaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoTaskList
        fields = ['name', 'description', 'deadline', "user"]