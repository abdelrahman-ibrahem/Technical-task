from django.db import models
from lists.models import ListModel

# create tasks model but remmber subtasks

class Priority(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title  = models.CharField(max_length=200)
    is_compeleted = models.BooleanField(default=False)
    list_id = models.ForeignKey(ListModel , on_delete=models.CASCADE)
    created  = models.DateTimeField(auto_now_add=True , null=True , blank=True)
    note = models.TextField(null=True , blank=True)
    location = models.CharField(max_length=255)
    priority  = models.ForeignKey(Priority , on_delete=models.CASCADE)
    subtask  = models.ManyToManyField('self'  , related_name='subtasks')
    def __str__(self):
        return self.title 
    