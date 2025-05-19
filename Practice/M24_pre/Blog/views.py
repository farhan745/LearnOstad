from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category,Tag
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login, logout 
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def post_list(request):
    categoryQ = request.GET.get('category', None)
    tagQ = request.GET.get('tag', None)
    
    if categoryQ:
        posts = Post.objects.filter(category_id__name=categoryQ)  # Assuming a foreign key with "name" in Category
    elif tagQ:
        posts = Post.objects.filter(tag__name=tagQ)  # Assuming a many-to-many relationship with Tag model
    else:
        posts = Post.objects.all()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags
    })
@login_required
def post_details(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request, 'blog/post_details.html', {'post':post})

def signup_view(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form':form})

@login_required
def post_edit(request,id):
    post = get_object_or_404(Post,id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        
        print(post.author_id)
        if request.user != post.author_id:
            messages.warning(request, "You do not have permission to edit this post")
            return redirect('post_details',id =post.id) 
        if form.is_valid():
            form.save()
            messages.success(request,"Successfully Edited")
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
            

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Do not save the instance yet
            post.author_id = request.user  # Assign the logged-in user as the author
            post.save()  # Save the instance now
            messages.success(request,"Successfully Created")
            return redirect('post_list')  # Redirect to the post list or any desired page
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})
@login_required
def post_delete(request,id):
    post=get_object_or_404(Post,id=id)
    if request.user != post.author_id:
        messages.warning(request, "You do not have permission to delete this post")
        return redirect('post_details',id =post.id)
    post.delete()
    messages.warning(request,"Successfully Deleted")
    return redirect('post_list')