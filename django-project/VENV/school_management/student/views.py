from django.shortcuts import render
from django.http import HttpResponse
from . import models


# def home(request):
#   return render(request,'index.html')
def profile(request):
    user_data = {
        "name": "John Doe",
        "age": 17,
    }
    mark = [
        {"id": 1, "subject": "Math", "marks": 90},
        {"id": 2, "subject": "English", "marks": 55},
        {"id": 3, "subject": "Science", "marks": 75},
        {"id": 4, "subject": "Social Studies", "marks": 60},
    ]
    student_data = models.Student.objects.all()
    print(student_data)
    # return render(request,'student/index.html',user_data)
    return render(
        request,
        "student/index.html",
        {
            "marks": mark,
            "age": 20,
            "Name": "Abdullah Ramadan shader",
            "ls": ["apple", "banana", "orange"],
            "student_data": student_data,
        },
    )


def home(request):
    return HttpResponse("I am Home Page")


def delete_student(request, id):
    student = models.Student.objects.get(id=id)
    student.delete()
    return HttpResponse("Student Deleted")
