from django.db import models
from django.contrib.auth import get_user_model


# create list model
class ListModel(models.Model):
    user = models.ForeignKey(get_user_model() , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    descrption = models.TextField(null=True , blank=True)


    def __str__(self):
        return self.title