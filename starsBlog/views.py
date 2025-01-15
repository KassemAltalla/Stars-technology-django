from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from .models import Post, Category, Author, Tag, Section, Image
from .serializers import (
    PostSerializer, PostDetailSerializer,
    CategorySerializer, AuthorSerializer, TagSerializer,
    SectionSerializer, ImageSerializer
)

# View لعرض وإنشاء المقالات
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        # حفظ المقالة ثم إضافة الأقسام والصور
        post = serializer.save()
        sections_data = self.request.data.get('sections', [])
        images_data = self.request.data.get('images', [])

        for section_data in sections_data:
            Section.objects.create(post=post, **section_data)

        for image_data in images_data:
            Image.objects.create(post=post, **image_data)

# View لعرض وتحديث وحذف مقالة معينة
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

    def perform_update(self, serializer):
        # تحديث المقالة ثم تحديث الأقسام والصور
        post = serializer.save()
        sections_data = self.request.data.get('sections', [])
        images_data = self.request.data.get('images', [])

        # تحديث الأقسام
        post.sections.all().delete()  # حذف الأقسام القديمة
        for section_data in sections_data:
            Section.objects.create(post=post, **section_data)

        # تحديث الصور
        post.images.all().delete()  # حذف الصور القديمة
        for image_data in images_data:
            Image.objects.create(post=post, **image_data)

# View لعرض المقالات الأحدث
class LatestPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.order_by('-publish_date')[:10]  # آخر 10 مقالات

# View لعرض المقالات الأكثر مشاهدة
class MostViewedPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.order_by('-views_count')[:10]  # أكثر 10 مقالات مشاهدة

# View لعرض المقالات في تصنيف معين
class CategoryPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        return Post.objects.filter(category__name=category_name)

# View لعرض المقالات التي كتبها كاتب معين
class AuthorPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        author_id = self.kwargs['author_id']
        return Post.objects.filter(author__id=author_id)

# View لعرض المقالات التي تحتوي على علامة معينة
class TagPostsView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag_name = self.kwargs['tag_name']
        return Post.objects.filter(tags__name=tag_name)

# View لعرض جميع التصنيفات مع عدد المقالات في كل تصنيف
class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.annotate(post_count=Count('post'))

# View لعرض جميع الكُتّاب
class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

# View لعرض جميع العلامات
class TagListView(generics.ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

# View لزيادة عدد مشاهدات مقالة معينة
class IncrementPostViewsView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.views_count += 1
        post.save()
        return Response({"message": "Views count incremented successfully."})

# View لإضافة قسم جديد إلى مقالة معينة
class AddSectionToPostView(APIView):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        section_data = request.data
        section_data['post'] = post.id
        serializer = SectionSerializer(data=section_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View لإضافة صورة جديدة إلى مقالة معينة
class AddImageToPostView(APIView):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        image_data = request.data
        image_data['post'] = post.id
        serializer = ImageSerializer(data=image_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)