from django.urls import path
from .views import TaskCreate, TaskDetail, TaskList, TaskUpdate

urlpatterns = [ 
    path("", TaskList.as_view(), name='tasks'),
    path("task/<int:pk>/", TaskDetail.as_view(), name = "task"),
    path("create-task/", TaskCreate.as_view(), name = "create-task"),
    path("edit-task/<int:pk>/", TaskUpdate.as_view(), name = "edit-task"),
]