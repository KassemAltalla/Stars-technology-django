from django.db import models
from django.utils import timezone

# Create your models here.


    ################################################################
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    post_count = models.IntegerField(default=0)  # حقل لتخزين عدد المقالات

    def __str__(self):
        return self.name

    def update_post_count(self):
        self.post_count = self.post_set.count()  # تحديث عدد المقالات بناءً على العدد الحالي للمقالات
        self.save()

################################################################

class Author(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    def __str__(self):
        return self.name
    
    ################################################################

class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    


class Post(models.Model):
    LANGUAGE_CHOICES = (
        ('AR', 'Arabic'),
        ('EN', 'English'),
    )

    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    publish_date = models.DateTimeField(default=timezone.now)
    views_count = models.IntegerField(default=0)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='EN')

    def __str__(self):
        return self.title
    
################################################################

class Section(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='sections')
    content = models.TextField()
    order = models.IntegerField(default=0)  # لترتيب الأقسام

    class Meta:
        ordering = ['order']  # ترتيب الأقسام بناءً على الحقل `order`

    def __str__(self):
        return f"Section {self.order} of {self.post.title}"
    
################################################################

class Image(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='images')
    image_url = models.URLField()
    order = models.IntegerField(default=0)  # لترتيب الصور

    class Meta:
        ordering = ['order']  # ترتيب الصور بناءً على الحقل `order`

    def __str__(self):
        return f"Image {self.order} of {self.post.title}"
    