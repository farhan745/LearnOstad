from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, TaskForm
from django.contrib import messages
from django.contrib.auth import login,logout
from .models import Task


# Create your views here.


def hello(request):
    return HttpResponse("Hello, world. You're at the todoapp index.")


@login_required
def hello_protected(request):
    user = request.user
    return render(request, "todoapp/protected.html", {"user": user})
    # return HttpResponse(
    #     "Hello, world. You're at the todoapp index. This page is protected."
    # )


def index(request):
    return HttpResponse("Welcome")


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            login(request, user)
            messages.add_message(request, messages.INFO, "User registered successfully!", extra_tags="registered")
            return redirect("task_list")
        else:
            messages.error(request, "There was an error in your registration form.")
    else:
        form = UserRegistrationForm()
    return render(request, "todoapp/register.html", {"form": form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "todoapp/task_list.html", {"tasks": tasks,"user":request.user})




@login_required
def task_edit(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)  # Ensure the task belongs to the current user
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, "Item edited successfully!", extra_tags="edited")
            return redirect('task_list')  # Redirect to the task list after saving
    else:
        form = TaskForm(instance=task)  # Populate the form with the existing task
        messages.error(request, "Edited unsuccessfully")
    return render(request, 'todoapp/create_task.html', {'form': form})
    

@login_required
def custom_logout(request):
    logout(request)
    return redirect('login')
@login_required
def create_task(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.add_message(request, messages.INFO, "Item created successfully!", extra_tags="created")
            return redirect('task_list')
        else:
            messages.error(request, "Failed to create the task. Please try again.")
    return render(request, 'todoapp/create_task.html', {"form": form})


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.add_message(request, messages.INFO, "Item deleted successfully!", extra_tags="deleted")
    else:
        messages.add_message(request, messages.ERROR, "Item deleted unsuccessfully!", extra_tags="deleted")
    return redirect('task_list')

    