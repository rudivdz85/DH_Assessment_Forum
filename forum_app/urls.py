from django.urls import path
from .views import PostList, LikePost, UserList, PostLikeList, PostDetail

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_id>/like/', LikePost.as_view(), name='like-post'),
    path('users/', UserList.as_view(), name='user-list'),
    path('posts/<int:post_id>/likes/', PostLikeList.as_view(), name='post-like-list'),
]