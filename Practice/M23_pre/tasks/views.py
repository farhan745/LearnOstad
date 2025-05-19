from django.shortcuts import render, redirect
from .models import Task
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    tasks = Task.objects.all()
    return render(request, 'index.html',{
        'tasks': tasks,
    })

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        completed = False
        
        if title != "" and due_date !="" and due_time != "":
            task = Task(
                title = title,
                description = description,
                due_date = due_date,
                due_time = due_time,
                completed = completed
            )
            task.save()
            return redirect('home')
    else:
        return render(request, 'add_task.html')
    return render(request, 'add_task.html')

@login_required
def completed(request):
    completed_tasks = Task.objects.filter(completed=True)
    return render (request, 'completed.html',{
        'tasks': completed_tasks,
    })

@login_required  
def remaining(request):
    remaining_tasks = Task.objects.filter(completed=False)
    return render (request, 'remaining.html',{
        'tasks': remaining_tasks,
    })

@login_required
def task_detail(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'task_detail.html',{
        'task': task,
    })
 
@login_required   
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    return render(request, 'delete.html',{
        'task': task,
    })

@login_required   
def toggle_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('home')

@login_required
def remove_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if len(password)<3:
            messages.error(request, 'Password must be at least 3 characters')
            return redirect('register')
        get_all_users_by_username = User.objects.filter(username=username)
        if get_all_users_by_username:
            messages.error(request,'Username already exists')
            return redirect('register')
        
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, 'User created successfully')
        return redirect('login')
    return render(request, 'register.html', {})

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =='POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        validate_user = authenticate(username=username, password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong User details')
            return redirect('login')
    return render(request, 'login.html', {})

def LogoutView(request):
    logout(request)
    return redirect('login')