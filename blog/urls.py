from django.urls import path
from .views import BlogPostList, BlogPostDetail, BlogPostCreate

urlpatterns = [
    path('', BlogPostList.as_view(), name='blogposts'),
    path('<int:pk>/', BlogPostDetail.as_view(), name='blogpost'),
    path('create/', BlogPostCreate.as_view(), name='blogpost'),
]
