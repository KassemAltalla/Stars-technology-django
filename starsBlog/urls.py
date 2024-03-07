from .views import get_posts,home,trend,category_post,get_article
from django.urls import path,include

urlpatterns = [
    path('posts',get_posts,name='get_posts'),
    path('',home,name='home'),
    path('trend',trend,name='trend'),
    path('category/<str:category_name>/',category_post,name='category_post'),
    path('article/<int:id>/',get_article,name='get_article'),
]