from django.contrib import admin
from .models import ListModel

@admin.register(ListModel)
class CustomAdmin(admin.ModelAdmin):
    list_display = ['user' , 'title' , 'descrption']
    search_fields = ['title']
