# crud/settings.py - 앱등록
INSTALLED_APPS = [
    ...,
    'posts',
]

# posts/admin.py - createsuperuser
from django.contrib import admin
from .models import Post

admin.site.register(Post)


# crud/urls.py - 경로 설정
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Read
    path('index/', views.index),
    path('posts/<int:id>/', views.detail),

    # Create
    path('posts/new/', views.new),
    path('posts/create/', views.create),

    # Delete
    path('posts/<int:id>/delete/', views.delete),

    # Update
    path('posts/<int:id>/edit/', views.edit),
    path('posts/<int:id>/update.', views.update),
]

# posts/views.py - 함수
from django.shortcuts import render, redirect
from .models. import Post

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)


def detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'detail.html', context)


def new(request):
    return render(request, 'new.html')


def craete(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')


def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/index/')


def edit(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post,
    }
    return render(request, 'edit.html', context)


def update(request, id):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')