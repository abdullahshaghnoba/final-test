from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Project(models.Model):
    project_name = models.CharField(max_length=256)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)
    total_cost = models.IntegerField(default=0) # this is the total cost of all tasks in the project

    def __str__(self):
        return self.project_name
    
class Task(models.Model):
    task_name = models.CharField(max_length=256)
    task_desc = models.CharField(max_length=1000)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    contributor = models.JSONField(default=list, null=True, blank=True)
    start_date = models.DateTimeField(default=None)
    end_date = models.DateTimeField(default=None)

    def __str__(self):
        return self.task_name
    
class Message(models.Model):
    comment = models.CharField(max_length=1000)
    # start_date = models.DateTimeField(default=None)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.comment