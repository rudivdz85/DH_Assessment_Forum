from rest_framework import serializers
from .models import Post, Like
from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']