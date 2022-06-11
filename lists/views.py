from django.shortcuts import render
from .models import ListModel
from rest_framework import generics
from .serializers import ListSerializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from permissions import permission
from django_filters.rest_framework import DjangoFilterBackend

# create and display lists
# get list and update it 


class GetAllListsAndCreateList(generics.ListCreateAPIView):
    queryset = ListModel.objects.all()
    serializer_class = ListSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']
    permission_classes  = [IsAuthenticatedOrReadOnly]


class GetSingleListAndUpdateOrDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ListModel.objects.all()
    serializer_class = ListSerializers
    permission_classes = [IsAuthenticatedOrReadOnly , permission.IsAuther]