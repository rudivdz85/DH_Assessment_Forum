from django.urls import path
from .views import PostList, LikePost, UserList

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:post_id>/like/', LikePost.as_view(), name='like-post'),
    path('users/', UserList.as_view(), name='user-list'),
]