from django.urls import path
from . import views


urlpatterns = [
    path('' , views.GetAllTasksAndCreate.as_view()),
    path('<int:pk>/' , views.GetSingleTaskAndUpdateOrDelete.as_view()),
    path('<int:pk>/subtasks' , views.GetSubTasks.as_view()),
    path('tasks-by-list/<int:list_id>/' , views.GetAllTasksByList.as_view()),
]