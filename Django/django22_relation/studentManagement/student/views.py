from django.shortcuts import render, HttpResponse, redirect
from . import models
from . import forms
from django.contrib import messages
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def create_student(request):
    form = forms.StudentForm()
    if request.method == "POST":  # 1. user post request koreche
        form = forms.StudentForm(
            request.POST, request.FILES
        )  # 2. user er post request capture korlam
        if form.is_valid():  # 3. user input validation kortechi
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Student Created Successfully"
            )  # 4. user input save korlam
            return redirect("home")
    else:
        form = forms.StudentForm()

    return render(request, "students/create_edit_student.html", {"form": form})


class CreateStudent(LoginRequiredMixin,CreateView):
    form_class = forms.StudentForm
    success_url = reverse_lazy("home")
    template_name = "students/create_edit_student.html"

    def form_valid(self, form):
        student = form.save(commit=False)# dataBase e data save hobe na kintu ami form er modde user er submit kora sob data paye jabo
        student.user = self.request.user# user_id save kora jaye
        student.save()
        messages.add_message(
            self.request, messages.SUCCESS, "Student Created Successfully"
        )
        return super().form_valid(form)


def home(request):
    student = models.Student.objects.all()
    return render(request, "students/index.html", {"students": student})


class StudentLists(ListView):
    model = models.Student
    template_name = "students/index.html"
    context_object_name = "students"


# This is for HTML forms
"""def home(request):
    print(request.POST)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        checkbox = request.POST.get("checkbox")
        photo = request.FILES.get("photo")
        if checkbox == "on":
            checkbox = True
        else:
            checkbox = False
        student = models.Student(
            name=name,
            email=email,
            phone=phone,
            password=password,
            checkbox=checkbox,
            photo=photo
        )  # student class er object
        student.save()  # student class er object save korlam
        return HttpResponse("Student Added Successfully")
    return render(request, "students/index.html")


"""


def display(request):
    return HttpResponse("<h1>Go to Home Page</h1>")


def update_student(request, id):
    student = models.Student.objects.get(id=id)
    form = forms.StudentForm(
        instance=student
    )  # user er ager data diye form fill korlam

    # form = forms.StudentForm()
    if request.method == "POST":  # user post request korse
        form = forms.StudentForm(
            request.POST, request.FILES, instance=student
        )  # user er data diye form fill korlam
        if form.is_valid():  # user input validation korte hobe
            form.save()  # user input save korlam
            messages.add_message(
                request, messages.SUCCESS, "Student updated successfully"
            )
            return redirect("home")

    return render(
        request, "students/create_edit_student.html", {"form": form, "edit": True}
    )


class UpdateStudentData(LoginRequiredMixin,UpdateView):
    form_class = forms.StudentForm
    model = models.Student
    template_name = "students/create_edit_student.html"
    success_url = reverse_lazy("home")
    pk_url_kwarg = "id"

    def form_valid(self, form):

        messages.add_message(
            self.request, messages.SUCCESS, "Student updated successfully"
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["edit"] = True
        return context


def delete_student(request, id):
    student = models.Student.objects.get(
        id=id
    )  # id=id er student object khuje ber korlam, jeta delete korbo
    student.delete()  # student object delete korlam
    messages.add_message(request, messages.SUCCESS, "Student deleted successfully")
    return redirect("home")  # home page e redirect korlam


class DeleteStudent(LoginRequiredMixin,DeleteView):
    model = models.Student
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")
    template_name = "students/delete_student.html"

    def delete(self, request, *args, **kwargs):
        messages.add.message(request, messages.SUCCESS, "Student deleted successfully")
        return super().delete()


def signup(request):
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Account Create Successfully"
            )
            return redirect("home")
    else:
        form = forms.SignUpForm(request.POST)
    return render(request, "students/auth_form.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user != None:
                login(request,user)
                messages.add_message(request,messages.SUCCESS,"Login Successful")
                return redirect("home")
            else:
                messages.add_message(request,messages.ERROR,"Invalid Username or Password")
    else:
        form = AuthenticationForm()
    return render(request, "students/auth_form.html", {"form": form})


def user_logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,"Logout Successful")
    return redirect("home")

@login_required
def user_profile(request):
    students = models.Student.objects.filter(user = request.user)
    return render(request, "students/profile.html", {"students": students})