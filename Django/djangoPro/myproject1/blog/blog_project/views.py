from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    return HttpResponse("<h1>Blog Home</h1>")

def demo(request):
    return render(request, 'index.html')
def post_list(request):
    posts = Post.objects.all()
    for post in posts:
        print(post.title)
    return HttpResponse("<h1>Post List</h1>")
