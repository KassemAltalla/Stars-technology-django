from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    section1 = models.TextField()
    section2 = models.TextField()
    section3 = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    publish_date = models.DateTimeField(default=timezone.now)  # حقل تاريخ النشر
    views_count = models.IntegerField(default=0)  # حقل عدد المشاهدات
    def __str__(self):
        return self.title