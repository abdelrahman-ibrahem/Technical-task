from .models import Priority , Task 
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id' , 'is_compeleted' , 'list_id' , 'created' , 'location' , 'note' , 'priority']
