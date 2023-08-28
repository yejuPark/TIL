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