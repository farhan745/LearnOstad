from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, TaskForm

from django.contrib.auth import login
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
            # set staff status to True
            user.is_staff = True
            user.save()
            login(request, user)
            return redirect("login")
            # return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, "todoapp/register.html", {"form": form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "todoapp/task_list.html", {"tasks": tasks})