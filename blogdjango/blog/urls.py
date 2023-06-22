from django.urls import path
from .views import Home, Posts, PostDetail, AddPost, UpdatePost, DeletePost, AddComment, Categories, CategoryDetail


urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('posts/', Posts.as_view(), name="posts"),
    path('post/<int:pk>', PostDetail.as_view(), name="post-detail"),
    path('add_post/', AddPost.as_view(), name="add_post"),
    path('post/edit/<int:pk>', UpdatePost.as_view(), name="update_post"),
    path('post/<int:pk>/delete', DeletePost.as_view(), name="delete_post"),
    path('post/<int:pk>/comment', AddComment.as_view(), name="add_comment"),
    path('posts/categories/', Categories.as_view(), name="categories"),
    path('posts/categories/<int:cat_id>', CategoryDetail, name="category-detail"),
]