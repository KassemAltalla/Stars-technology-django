from django.contrib import admin
from .models import Category, Author, Tag, Post, Section, Image

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Section)
admin.site.register(Image)