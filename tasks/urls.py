from django.urls import path
from tasks.views import *

urlpatterns = [
    path('',register_page,name='register_page'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),

    path('home/', home_page, name='home_page'),
    path('task_list/', task_list, name='task_list'),
    path('add-task/', add_task, name='add_task'),
    path('update-task/<str:t_id>/', update_task, name='update_task'),
    path('delete-task/<str:t_id>/', delete_task, name='delete_task'),
    path('view-task/<str:t_id>/', view_task, name='view_task'),
         
]

