from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def user_sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    form = UserCreationForm()
    return render(request,'first_app/signup.html',{'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password"]
            user=authenticate(username= username, password=password)
            login(request, user)
            return redirect("home")
    form = AuthenticationForm()
    return render(request,'first_app/login.html',{'form':form})
def home(request):
    return render(request,'first_app/home.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect("login")
@login_required
def pass_change(request):
    form = PasswordChangeForm(request.user)
    return render(request,'first_app/change_pass.html',{'form':form})
        