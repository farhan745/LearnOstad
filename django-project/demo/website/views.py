from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, "home.html")


def about(request):
    return HttpResponse("This is about Page")


def contact(request):
    return HttpResponse("This is Contact Page")
