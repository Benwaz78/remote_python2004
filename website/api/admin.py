from django.contrib import admin
from api.models import ImageCategory, ImageSearch

# Register your models here.

admin.site.register(ImageSearch)
admin.site.register(ImageCategory)
