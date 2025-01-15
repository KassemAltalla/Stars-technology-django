from django.contrib import admin


from .models import (
    UserProfile, Category, Brand, Product,
    ProductImage, ProductOption, Cart, CartItem,
    Order, OrderItem
)

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductOption)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)