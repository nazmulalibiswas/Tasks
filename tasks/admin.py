from django.contrib import admin
from tasks.models import CustomUserInfoModel, TaskModel 

admin.site.register([CustomUserInfoModel,TaskModel])



