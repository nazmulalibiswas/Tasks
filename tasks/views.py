from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from tasks.models import*
from tasks.forms import *

def register_page(request):
  if request.method == 'POST':
    full_name = request.POST.get('full_name')
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    
    if password == confirm_password:
      CustomUserInfoModel.objects.create_user(
        full_name = full_name,
        username = username,
        email = email,
        password = password,
      )
      return redirect('login_page')

  return render(request, 'register.html')

def login_page(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate (request, username = username, password = password)
    if user:
      login (request, user)
      return redirect('home_page')
    else:
      print("Invalid credentials.")
  
  return render(request, 'login.html')

@login_required
def logout_page(request):
  logout(request)
  return redirect ('login_page')

@login_required
def home_page(request):

  return render(request, 'home.html')

@login_required
def task_list(request):
  task_data = TaskModel.objects.all()

  context = {
    'task_data' : task_data
  }
  
  return render(request, 'task-list.html', context)

@login_required
def add_task (request):
  if request.method == 'POST':
    form_data = TaskForm(request.POST)
    form_data.save()
    return redirect ('task_list')
  
  form_data = TaskForm()
  context = {
    'form_data':form_data,
    'form_title': 'Add Task Info',
    'btn_name' : 'Add Task',
  }

  return render(request, 'master/base-form.html', context)

@login_required
def update_task(request, t_id):
  task_data = get_object_or_404(TaskModel, id=t_id)
  if request.method == 'POST':
    form_data = TaskForm(request.POST, instance=task_data)
    form_data.save()
    return redirect ('task_list')

  form_data = TaskForm(instance=task_data)
  context = {
    'form_data':form_data,
    'form_title': 'Update Task Info',
    'btn_name' : 'Update Task',
  }
  return render(request, 'master/base-form.html', context)

@login_required
def delete_task(request, t_id):
  get_object_or_404(TaskModel, id=t_id).delete()
  return redirect ('task_list')

@login_required
def view_task(request, t_id):
  task_data = get_object_or_404(TaskModel, id=t_id)
  context = {
    'task_data': task_data
  }
  return render (request, 'task-detail.html', context)




