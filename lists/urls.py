from django.urls import path 
from . import views

urlpatterns = [
    path('' , views.GetAllListsAndCreateList.as_view()),   
    path('<int:pk>' , views.GetSingleListAndUpdateOrDelete.as_view()),   
]