from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post
from .forms import PostForm, LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = "Invalid username or password"
        else:
            error_message = "Form data is not valid"
    else:
        form = LoginForm()
        error_message = None
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

@login_required
def home(request):
    posts = Post.objects.all()

    # Filtering
    sort_by_date = request.GET.get('sort_by_date')
    if sort_by_date:
        posts = posts.order_by('created_at' if sort_by_date == 'oldest' else '-created_at')

    media_type = request.GET.get('media_type')
    if media_type:
        if media_type == 'text':
            posts = posts.filter(image__isnull=True)
        elif media_type == 'image':
            posts = posts.filter(image__isnull=False)

    author = request.GET.get('author')
    if author:
        posts = posts.filter(user__username=author)

    # Search
    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))

    return render(request, 'home.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})
