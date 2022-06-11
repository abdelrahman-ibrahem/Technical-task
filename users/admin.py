from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomizeCustomUser(admin.ModelAdmin):
    list_display = ['username' , 'email'  , 'name']
