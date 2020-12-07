from django.contrib import admin
from frontend.models import Category, Post, UserProfile

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(UserProfile)
