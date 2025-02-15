from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse

# Create your views here.

def user_from(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponse("Successfully created")
  else:
    form = UserCreationForm()
  return render(request,'first_app/sign_up.html',{'form':form})