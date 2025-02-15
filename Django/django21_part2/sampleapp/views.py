from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import TaskForm


# Create your views here.
def form_view(request):
    # if request.method == 'POST':
    #   print(request.POST.dict())
    #   return JsonResponse({'massage':"Form Submitted successfully"})

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
            return render(request, "form.html", context)
    form = TaskForm()
    context = {
        "myform": form,
    }
    return render(request, "form.html", context)
