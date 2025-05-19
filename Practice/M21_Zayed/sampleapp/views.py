from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views import View
from django.views.generic import CreateView
from .forms import TaskForm
from . import models

class TaskCreateView(View):
    form_class = TaskForm

    def get(self, request):
        form = self.form_class()
        context = {
            "myform": form,
        }
        messages.success(request, "Task created successfully")
        return render(request, "task_create.html", context)
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Form Submitted successfully</h1>")
        else:
            form = self.form_class()
            context = {
                "myform": form,
            }
            return render(request, "task_create.html", context)

class TaskCreateReadymadeView(CreateView):
    model = models.Task
    form_class = TaskForm
    template_name = 'task_create.html'
    success_url = '/'
    context_object_name = 'form'

def form_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Form Submitted successfully</h1>")
        else:
            form = TaskForm()
            context = {
                "myform": form,
            }
            return render(request, "task_create.html", context)
    else:
        form = TaskForm()
        context = {
            "myform": form,
        }
        return render(request, "task_create.html", context)
