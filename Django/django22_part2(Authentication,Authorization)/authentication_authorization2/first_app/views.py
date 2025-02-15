from django.shortcuts import render,redirect,HttpResponse
from  django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def user_signup(request):
    
    if request.method == 'POST':# ! user req post hoyse
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully created")
    form = UserCreationForm() # ! abr nutun kore start
    return render(request,'first_app/signup.html',{'form':form})
@csrf_exempt
def user_login(request):
    
    if request.method == 'POST':# ! user req post hoyse
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
           print(form.cleaned_data)
           username = form.cleaned_data['username']
           password = form.cleaned_data['password']
           user = authenticate(username=username, password=password)
           print(user)
           login(request,user)
           return HttpResponse("Successfully Login")
    else:
        form = AuthenticationForm() # ! abr nutun kore start
    return render(request,'first_app/signup.html',{'form':form})

def user_logout(request):
    logout(request)
    return HttpResponse('Log Out Successful')
@login_required
def password_change(request):
    form = PasswordChangeForm(request.user)
    return render(request,'first_app/pass.html',{'form':form})