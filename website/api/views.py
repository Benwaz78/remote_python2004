from django.shortcuts import render
from frontend.models import Post, Category
from django.contrib.auth.models import User
from rest_framework import viewsets
from api.serializers import PostSerializer, UserSerializer, CategorySerializer


# Create your views here.


class PostView(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class UserView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer


class CategoryView(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer


