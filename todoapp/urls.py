from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, filter_form, filter_task

urlpatterns = [
    path('', TaskList.as_view(), name='tasklist'),
    path('task/<int:pk>', TaskDetail.as_view(), name='taskdetail'),
    path('create/', TaskCreate.as_view(), name='taskcreate'),
    path('update/<int:pk>', TaskUpdate.as_view(), name='taskupdate'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='taskdelete'),
    path('filter_form', filter_form, name='filter_form'),
    path('filter_task', filter_task, name='filter_task'),
]
