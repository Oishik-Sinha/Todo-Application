from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class todoTaskList(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=500, null=False)
    description = models.CharField(max_length=5000)
    deadline = models.DateTimeField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    one_day_notification = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "todo_task_list"

    def __str__(self):
        return f"{self.id} -> {self.name}"
