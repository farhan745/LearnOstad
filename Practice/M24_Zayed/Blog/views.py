from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Category,Tag,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login, logout 
from .forms import PostForm,CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Count

@login_required
def post_list(request):
    categoryQ = request.GET.get('category', None)
    tagQ = request.GET.get('tag', None)
    search_query = request.GET.get('q', None)
    
    # Base QuerySet
    posts = Post.objects.all().order_by('-created_at')
    
    if categoryQ:
        posts = posts.filter(category_id__name=categoryQ)  # Correcting this lookup to `category_id__name`
    elif tagQ:
        posts = posts.filter(tag__name=tagQ)  # This is correct
    
    if search_query:
        posts = posts.filter(
        Q(title__icontains=search_query) |
        Q(content__icontains=search_query) |
        Q(category_id__name__icontains=search_query) |  # Correct lookup
        Q(tag__name__icontains=search_query) |  # Correct lookup
        Q(author_id__username__icontains=search_query)  # Fixed lookup for author username
        )
    
    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'blog/post_list.html', {
        'posts': posts,
        'categories': categories,
        'tags': tags
    })

@login_required
def post_details(request, id):
    post = get_object_or_404(Post.objects.annotate(comment_count=Count('comment')), id=id)
    cat = Category.objects.all()
    tags = Tag.objects.all()

    # Track the logged-in user's comments
    user_comments = post.comment_set.filter(author=request.user)

    comment_form = CommentForm()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.success(request, "Successfully Commented")
            return redirect('post_details', id=post.id)

    comments = post.comment_set.all()
    if request.user.id not in post.viewed_users:
        post.view_count += 1
        post.viewed_users.append(request.user.id)
        post.save()
        
    is_liked=False
    if post.liked_user.filter(id=request.user.id):
        is_liked=True
    else:
        is_liked=False
    like_count = post.liked_user.count()
    return render(request, 'blog/post_details.html', {
        'post': post,
        'categories': cat,
        'tags': tags,
        'comments': comments,
        'comment_form': comment_form,
        'comment_count': post.comment_count,
        'user_comments': user_comments,  # Pass user's comments to the template
        'is_liked':is_liked,
        'like_count':like_count,
    })

def signup_view(request):
    if request.method=="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            messages.success(request,"New user created successfully and logged in successfully")
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


#todo: like Group
@login_required
def Like_post(request,id):
    post=get_object_or_404(Post,id=id)
    if request.user not in post.liked_user.all():
        post.liked_user.add(request.user)
        messages.success(request, "Successfully liked")
    else:
        post.liked_user.remove(request.user)
        messages.success(request, "Successfully unliked")
        
    return redirect('post_details', id=post.id)