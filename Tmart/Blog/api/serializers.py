from rest_framework import serializers
from Blog.models import BlogModel

# class TagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tag
#         fields = ('id', 'name')

class BlogSerializer(serializers.ModelSerializer):
    # tags = TagSerializer()
    created_by = serializers.SerializerMethodField()
    # tags = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return obj.created_by.username

    # def get_tags(self, obj):
    #     return [{'name': tag.name} for tag in obj.tags.all() ]

    class Meta:
        model = BlogModel
        fields = ('title', 'description', 'img', 'created_by')

class CreateBlogSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return obj.created_by.username

    class Meta:
        model = BlogModel
        fields = ('title', 'description', 'img', 'created_by')
