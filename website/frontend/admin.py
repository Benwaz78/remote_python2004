from django.contrib import admin
from frontend.models import Category, Post, UserProfile, About

# Register your models here.
admin.site.site_header = 'Django Class'
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(About)
