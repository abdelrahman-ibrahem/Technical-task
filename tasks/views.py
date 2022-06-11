from django.shortcuts import render
from .models import Task 
from rest_framework import generics
from .serializers import TaskSerializer 
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from lists.models import ListModel
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend



# get all tasks and create task
class GetAllTasksAndCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title' , 'is_compeleted' , 'list_id' , 'created' , 'note' , 'location' , 'priority']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# get single task and update ot and delete
class GetSingleTaskAndUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# get all tasks by list
class GetAllTasksByList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get (self ,  request , list_id , *args , **kwargs):
        try:
            list_pk = ListModel.objects.get(id =list_id)
            tasks = Task.objects.all().filter(list_id=list_pk)
            serializer = TaskSerializer(tasks , many=True)
            return Response(serializer.data)
        except:
            return Response({
                "message": 'Error'
            } , status=status.HTTP_400_BAD_REQUEST)


# get subtasks in task


class GetSubTasks(APIView):
    def get(self , request , pk , *args,**kwargs):
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(task)
            return Response(serializer.data['subtask'])
        except:
            return Response({
                "message": "ERROR"
            } , status=status.HTTP_404_BAD_REQUEST) 