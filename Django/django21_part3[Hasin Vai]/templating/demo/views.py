from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def data(request):
  first_name='Rahim'
  last_name='Hasan'
  context={'fname':first_name,'lname':last_name,"age":23}
  return render(request, 'index.html',context)
def loop(request):
  #data =['karim', 'hasan', 'rahim','jamal','kamal']
  data =[('karim',25), ('hasan',30), ('rahim',23),('jamal',21),('kamal',33),('Jitu',41)]
  number =55
  temperature = 43
  return render(request, 'loop.html',{'persons':data, 'temperature':temperature,'number':number})
def home(request):
  return render(request, 'data.html')
def about(request):
  return render(request, 'about.html')
def contact(request):
  return render(request, 'contact.html')
def reports(request):
  return render(request, 'reports.html')