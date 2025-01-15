from django.urls import path
from .views import (
    PostListCreateView, PostDetailView,
    LatestPostsView, MostViewedPostsView,
    CategoryPostsView, AuthorPostsView,
    TagPostsView
)

urlpatterns = [
    # جميع المقالات وإنشاء مقالة جديدة
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),

    # تفاصيل مقالة معينة (بناءً على الـ ID)
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),

    # المقالات الأحدث
    path('posts/latest/', LatestPostsView.as_view(), name='latest-posts'),

    # المقالات الأكثر مشاهدة
    path('posts/most-viewed/', MostViewedPostsView.as_view(), name='most-viewed-posts'),

    # المقالات في تصنيف معين
    path('category/<str:category_name>/posts/', CategoryPostsView.as_view(), name='category-posts'),

    # المقالات التي كتبها كاتب معين
    path('author/<int:author_id>/posts/', AuthorPostsView.as_view(), name='author-posts'),

    # المقالات التي تحتوي على علامة معينة
    path('tag/<str:tag_name>/posts/', TagPostsView.as_view(), name='tag-posts'),
]