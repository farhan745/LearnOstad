from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post,Tag , Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
def post_list(request):
    categoryQ = request.GET.get("category", None)
    tagQ = request.GET.get("tag", None)
    search_query = request.GET.get("q", None)

    if categoryQ:
        posts = Post.objects.filter(category__name=categoryQ)
    elif tagQ:
        posts = Post.objects.filter(tag__name=tagQ)
    else:
        posts = Post.objects.all()

    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query)
            | Q(content__icontains=search_query)
            | Q(tag__name__icontains=search_query)
            | Q(category__name__icontains=search_query)
        )

    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories, 'tags': tags})

def post_details(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_details.html', {'post': post})


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
        
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
        
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})
    
from django.contrib import messages  
@login_required
def post_update(request,id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        messages.error(request, 'You are not authorized to edit this post.')
        return redirect('post_details',id=post.id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,"")
            return redirect('post_details',id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_create.html', {'form': form})
        
        
def post_delete(request,id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        messages.error(request, 'You are not authorized to delete this post.')
        return redirect('post_details',id=post.id)
    post.delete()
    messages.success(request,"Post deleted successfully.")
    return redirect('post_list')