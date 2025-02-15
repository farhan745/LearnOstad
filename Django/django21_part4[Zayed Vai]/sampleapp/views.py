from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import TaskForm
from django.views import View
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.contrib import messages
# Create your views here.
class TaskCreateView(View):
    form_class = TaskForm
    
    def get(self, request):
        form = self.form_class()
        context = {
            "form": form,
        }
        messages.error(request, "Task created successfully")
        return render(request, "task_create.html", context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Form Submitted successfully</h1>")
        else:
            context = {
                "form": form,
            }
            return render(request, "task_create.html", context)

class TaskCreateReadyMadeView(CreateView):
    form_class = TaskForm
    template_name = "task_create.html"
    success_url = "/"
    context_object_name = "form"

def form_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Form Submitted successfully</h1>")
        else:
            context = {
                "form": form,
            }
            return render(request, "form.html", context)

    form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "task_create.html", context)
