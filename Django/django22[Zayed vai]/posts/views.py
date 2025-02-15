from django.shortcuts import render, HttpResponse
from .models import Post, Comment, Tag
from django.db import models

# Create your views here.
def index(request):
    """mypost = Post(
        title="Hello World",
        content="This is the first post",
        published=True,
    )
    mypost.save()"""
    # Create
    """Post.objects.create(title="Hello World 2",
                        content="This is the 2nd post",
                        published=False)"""

    # Read
    """posts=Post.objects.all()
    for post in posts:
        print(post.title)
        print(post.content)
        print(post.published)
    return HttpResponse("Hello World")"""

    # Filter
    """post = Post.objects.get(id=7)
    print(post.content)"""

    """posts = Post.objects.filter(published=False)
    print(posts)"""
    # Exclude
    """posts= Post.objects.all().exclude(published=True)
    print(posts)
    """

    # lookup
    """posts = Post.objects.filter(title__contains = "2")
    print(posts)
    posts1 = Post.objects.filter(id__in=[1,3])
    print(posts1)
    return HttpResponse("<h1 style='color:red'>Hello World</h1>")"""

    # updated [Single Post]
    """posts = Post.objects.get(id=3)
    posts.title = "Hello World3"
    posts.save()"""

    # updated [Multiple Posts] / Without Save function
    """  posts = Post.objects.filter(published = True)
    posts.update(published = False)"""
    # delete [Single Post]
    """post = Post.objects.get(id=11)
    post.delete()"""

    # delete [Multiple Posts]
    """post = Post.objects.all()
    post.delete()"""

    """Comment.objects.create(
        post_id = 1,
        content = "First Comment",
    )
    Comment.objects.create(
        post_id = 1,
        content = "Second Comment",
    )
    Comment.objects.create(
        post_id = 1,
        content = "Third Comment",
    )"""
    # Single Comment
    """comment = Comment.objects.get(id=2)
    print(comment.post)"""
    # Multiple Comments
    """ comments = Post.objects.get(id=1)
    print(comments.comment_set.all())"""
    # Tag Create
    """Tag.objects.create(
        name="Jushang"
    )"""

    # Tag Multifle Create
    """Tag.objects.bulk_create(
        [
            Tag(name="Python"),
            Tag(name="Django"),
            Tag(name="Flask"),
        ]
    )"""

    # Read Tag
    """
    tag1 = Tag.objects.get(id = 1)
    tag2 = Tag.objects.get(id = 2)
    post = Post.objects.get(id = 1)
    post.tags.add(tag1,tag2)
    print(tag1.posts.all())
    """

    # ? Advance Quary
    # ! Chain
    '''posts = (
        Post.objects.filter(published=True)
        .filter(title__icontains="my")
        .exclude(content__icontains="second")
    )'''
    
    # ! Order 
    # ! -> ascending Sorting
    '''posts = Post.objects.all().order_by("updated_at")
    print(posts)'''
    # ! -> descending Sorting
    ''' posts = Post.objects.all().order_by("-updated_at")
    print(posts)'''
    
    
    # ? Slicing
    '''posts = Post.objects.all()[:1]
    print(posts)'''
    
    # ? Or
    '''posts = Post.objects.filter(
        models.Q(title__icontains="my") | models.Q(content__icontains="post")
    )
    print(posts)'''
    
    
    # ? Filter Related Field
    posts = Post.objects.filter(tags__name="Python")
    print(posts)
    
    
    # ? Query Optimize 
    # ! Prefetch Related
    posts = Post.objects.all().prefetch_related("comments")
    
    for post in posts:
        print(post.title)
        
    return HttpResponse("<h1 style='color:red'>Hello World</h1>")
