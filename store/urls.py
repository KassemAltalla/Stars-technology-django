from django.urls import path
from .views import (
    UserProfileView, CategoryListView, ProductListView,
    ProductDetailView, CartView, OrderListView
)

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('orders/', OrderListView.as_view(), name='order-list'),
]