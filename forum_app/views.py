from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer, UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class PostList(APIView):
    """
    List all posts, or create a new post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    """
    Retrieve a single post by ID.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk, format=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)


class LikePost(APIView):
    """
    Like a post.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id, format=None):
        post = get_object_or_404(Post, pk=post_id)
        like, created = Like.objects.get_or_create(post=post, user=request.user)
        if created:
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class PostLikeList(APIView):
    """
    List all likes for a specific post.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, post_id, format=None):
        likes = Like.objects.filter(post__id=post_id)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)


class UserList(APIView):
    """
    List all users.
    """
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
