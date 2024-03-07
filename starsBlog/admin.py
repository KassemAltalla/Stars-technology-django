from django.contrib import admin
from .models import Category, Author, Tag, Post
# Register your models here.


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)