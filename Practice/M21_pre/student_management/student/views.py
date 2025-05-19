from django.shortcuts import render,redirect

from . import models
from . import forms
from django.contrib import messages
from . import forms

#!For Class View Model
from django.views.generic import ListView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
#todo: This is for HTML forms
'''def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        checkbox = request.POST.get('checkbox')
        photo = request.FILES.get('photo')
        if checkbox == 'on':
            checkbox = True
        else:
            checkbox = False
        student = models.Student(name=name, email=email, phone=phone, password=password, checkbox=checkbox,photo=photo)
        student.save()
        
        return render(request, 'student/index.html', {'message': 'Student saved successfully!'})

    return render(request, 'student/index.html')'''

#todo: This is for Models Form
@login_required
def create_student(request):
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.user = request.user
            student.save()
            messages.add_message(request, messages.SUCCESS, "Student saved successfully")
            return redirect(reverse_lazy('home'))
    else:
        form = forms.StudentForm()
    return render(request, 'student/create_student.html', {'form': form})
#!For Class base views
class CreateStudent(CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy('home')
    template_name = 'student/create_student.html'
    def form_valid(self, form):
        student = form.save(commit=False)
        student.user=self.request.user
        student.save()
        messages.add_message(self.request,messages.SUCCESS,"Student saved successfully")
        return super().form_valid(form)

def home(request):
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {"students": students})


#!For Class base views
class StudentList(ListView):
    model = models.Student
    template_name = 'student/index.html'
    context_object_name ='students'    
def update_student(request,id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(instance=student)
    #form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Student updated successfully")
            return redirect('home')
    return render(request, 'student/create_student.html',{'form':form,'edit':True})
#!Update Student Class Base
class UpdateStudentData(UpdateView):
    form_class =  forms.StudentForm
    model = models.Student
    template_name = 'student/create_student.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    def from_valid(self,form):
        
        messages.add_message(self.request,messages.SUCCESS,"Student updated successfully")
        return super().from_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['edit']=True
        return context
def delete_student(request,id):
    student = models.Student.objects.get(id=id)
    student.delete()
    messages.add_message(request,messages.SUCCESS,"Student deleted successfully")
    return redirect('home')

class DeleteStudent(DeleteView):
    model = models.Student
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = 'student/delete_student.html'
    def delete(self, request, *args, **kwargs):
        messages.add_message(request,messages.SUCCESS,'Student Deleted Successfully')
        return super().delete(request, *args, **kwargs)
    
def signup(request):
    form = forms.SignUpForm()
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"Account Created Successfully!")
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
            return redirect('signup')
    return render(request, 'student/auth_form.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, "Login Successfully!")
                return redirect('home')
            else:
                messages.error(request, 'Username or Password is incorrect')
        else:
            messages.error(request, 'Invalid form submission')
    else:
        form = AuthenticationForm()

    return render(request, 'student/login.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Logout Successfully!")
    return redirect('home')
@login_required
def profile(request):
    students = models.Student.objects.filter(user=request.user)
    return render(request, 'student/profile.html', {'students': students})