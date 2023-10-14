from django.urls import path

from todoManagement.views import todoViews

urlpatterns = [
    path('todo-list', todoViews.todoManager.as_view())
]

