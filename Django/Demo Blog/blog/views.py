from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Tag, Category, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

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

    return render(
        request,
        "blog/post_list.html",
        {"posts": posts, "categories": categories, "tags": tags},
    )


def post_details(request, id):
    post = get_object_or_404(Post, id=id)

    categories = Category.objects.all()
    tags = Tag.objects.all()
    comment_form = CommentForm()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
    # comment
    # comments = Comment.objects.filter(post = post)
    comments = post.comment_set.all()
    
    #!Liked Posts
    
    if post.liked_users.filter(id=request.user.id):
        is_liked = True
    else:
        is_liked = False
        
    like_count = post.liked_users.count()
    context = {
        "post": post,
        "categories": categories,
        "tags": tags,
        "comments": comments,
        "comment_form": comment_form,
        "is_liked": is_liked,
        'like_count':like_count,
    }
    post.view_count += 1
    post.save()
    return render(request, "blog/post_details.html", context)
@login_required
def like_post(request, id):
    post = get_object_or_404(Post, id=id)

    if post.liked_users.filter(id=request.user.id):
        post.liked_users.remove(request.user)
    else:
        post.liked_users.add(request.user)

    return redirect("post_details", id=post.id)
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")

    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})


@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post_list")

    else:
        form = PostForm()
    return render(request, "blog/post_create.html", {"form": form})


from django.contrib import messages


@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        messages.error(request, "You are not authorized to edit this post.")
        return redirect("post_details", id=post.id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "")
            return redirect("post_details", id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_create.html", {"form": form})


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.user != post.author:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect("post_details", id=post.id)
    post.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect("post_list")
