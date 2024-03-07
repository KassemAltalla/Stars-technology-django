from django.shortcuts import render
from django.http import JsonResponse
from .models import Post,Category
from django.shortcuts import get_object_or_404
# Create your views here.


def get_posts(request):
    Posts = Post.objects.all()
    data = {'Posts': list(Posts.values())}
    return JsonResponse(data)

def home(request):
    most_viewed_posts = Post.objects.order_by('-views_count')[:3]  # أكثر ثلاثة مقالات مشاهدة
    latest_posts = Post.objects.order_by('-publish_date')[:8]  # آخر ثمانية مقالات نشراً
    categories = Category.objects.all()  # جميع الفئات

    data = {
        'most_viewed_posts': list(most_viewed_posts.values()),
        'latest_posts': list(latest_posts.values()),
        'categories': list(categories.values())
    }
    return JsonResponse(data)

def trend(request):
    most_viewed_posts = Post.objects.order_by('-views_count')[:8]
    latest_posts = Post.objects.order_by('-publish_date')[:3]
    categories = Category.objects.all()  # جميع الفئات
    data = {
        'most_viewed_posts': list(most_viewed_posts.values()),
        'latest_posts': list(latest_posts.values()),
        'categories': list(categories.values())
    }
    return JsonResponse(data)

def category_post(request,category_name):
    category = get_object_or_404(Category, name=category_name)
    category_posts = Post.objects.filter(category=category).order_by('-publish_date')[:8]
    data = {
        'category_posts': list(category_posts.values()),
    }

    return JsonResponse(data)

def get_article(request,id):
    article=Post.objects.filter(id=id)
    data={
        'article':list(article.values())
    }
    return JsonResponse(data)