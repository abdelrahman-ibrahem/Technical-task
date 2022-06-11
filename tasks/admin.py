from django.contrib import admin
from .models import * 

admin.site.register(Priority)

@admin.register(Task)
class CustomizeTasks(admin.ModelAdmin):
    list_display = ['title' , 'note' , 'location' , 'is_compeleted' , 'created']
