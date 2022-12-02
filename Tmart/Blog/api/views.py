from Blog.models import BlogModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import BlogSerializer, CreateBlogSerializer
from django.http import Http404
from rest_framework import status

class BlogView(APIView):

    def get_object(self, pk):
        blog_qs = BlogModel.objects.filter(id=pk)
        if blog_qs.exists():
            return blog_qs.first()
        raise Http404

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            obj = self.get_object(pk)
            return Response(BlogSerializer(obj).data)

        blogs = BlogModel.objects.all()
        blogs_list = BlogSerializer(blogs, many=True).data
        return Response(blogs_list)

    def post(self, request, *args, **kwargs):
        new_blog_serializer = CreateBlogSerializer(data=request.data)
        if new_blog_serializer.is_valid():
            new_blog_serializer.save()
            return Response(new_blog_serializer.data)
        return Response(serializers.errors)

    def put(self, request, pk = None, *args, **kwargs):
        if pk:
            obj = self.get_object(pk)
            # return Response(BlogSerializer(obj).data) 
        blog_serializer = CreateBlogSerializer(data=request.data, instance=obj)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return Response(BlogSerializer[obj].data)
        return Response(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None, *args, **kwargs):
        if pk:
            obj = self.get_object(pk)
            # return Response(BlogSerializer(obj).data) 
        blog_serializer = CreateBlogSerializer(data=request.data, instance=obj, partial=True)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return Response(BlogSerializer[obj].data)
        return Response(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogDetailView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        blog_qs = BlogModel.objects.filter(id = pk)
        if not blog_qs.exists():
            raise Http404

        blog = blog_qs.first()
        deleted_count, _ = blog.delete()

        # blog.soft_delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
