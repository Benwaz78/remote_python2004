from frontend.models import Post, Category
from django.contrib.auth.models import User
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

	class Meta():
		model = Post
		fields = ('id', 'pst_title', 'pst_image',
		           'content', 'user', 'cat_id')


class CategorySerializer(serializers.ModelSerializer):

	class Meta():
		model = Category
		fields = ('id', 'cat_name', 'cat_desc')


class UserSerializer(serializers.ModelSerializer):

	class Meta():
		model = User
		fields = ('id', 'first_name', 'last_name', 'email')



