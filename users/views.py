from django.shortcuts import render
from .serializers import UserSerializers
from rest_framework.views import Response
from rest_framework import generics
from .models import CustomUser
from permissions import permission

# get user 
# update user 
class GetUserAndUpdate(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializers
    permission_classes = [permission.IsUser]
