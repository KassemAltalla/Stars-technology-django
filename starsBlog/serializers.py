from rest_framework import serializers
from .models import Post, Category, Author, Tag, Section, Image

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'content', 'order']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_url', 'order']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'author', 'tags', 'publish_date', 'views_count', 'language']

class PostDetailSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'category', 'author', 'tags', 'publish_date', 'views_count', 'language', 'sections', 'images']

class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'post_count']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'info']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']