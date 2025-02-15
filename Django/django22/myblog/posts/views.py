from django.shortcuts import render, HttpResponse
from posts.models import Post


# Create your views here.
def index(request):
    """Post.objects.create(
        title="My fourth post", content="This is my fourth post", published=False
    )
    Post.save()
    post = Post.objects.all()
    print(post)"""

    posts = Post.objects.get(id=1)
    posts.objects.update(published=False)

    return HttpResponse(posts)  # HttpResponse ekta class
