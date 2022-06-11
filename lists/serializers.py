from rest_framework import serializers
from .models import ListModel

class ListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListModel
        fields = '__all__'