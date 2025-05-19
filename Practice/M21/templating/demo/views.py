from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
def data(request):
    name="Rahim"
    age = 21
    person={'name': name,'age': age}
    return render(request, 'data.html',{"person":person} )
def loop(request):
    data = ['Karim','Rahim','Jamal','Kamal']
    data = [('Karim',24),("Rahim",25),("Jamal",21),("Kamal",18)]
    temperature = 40
    return render(request, 'loop.html',{'persons':data,'temperature':temperature})

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def report(request):
    return render(request, 'reports.html')