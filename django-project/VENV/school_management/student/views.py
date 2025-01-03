from django.shortcuts import render
from django.http import HttpResponse
# def home(request):
#   return render(request,'index.html')
def profile(request):
  user_data = {
    "name": "John Doe",
    "age": 17,
  }
  mark = [
    {
      "id":1,
      "subject": "Math",
      "marks": 90
    },
    {
      "id":2,
      "subject": "English",
      "marks": 55
    },
    {
      "id":3,
      "subject": "Science",
      "marks": 75
    },
    {
      "id":4,
      "subject": "Social Studies",
      "marks": 60
    }
    
  ]
  # return render(request,'student/index.html',user_data)
  return render(request,'student/index.html',{'marks':mark,'age':20,'Name':"Abdullah Rahaman Shikder"})