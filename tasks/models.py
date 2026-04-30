from django.db import models
from django.contrib.auth.models import AbstractUser

# username,full_name,email,password, confirm_password
class CustomUserInfoModel(AbstractUser):
    full_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.username}-{self.full_name}'
    
# title, description, status,(Pending, InProgress, Completed), due_date, created_at, updated_at

class TaskModel(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('InProgress', 'InProgress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    status = models.CharField(max_length=20, choices=STATUS, null=True)
    due_date = models.DateField(auto_now_add=True, null =True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
