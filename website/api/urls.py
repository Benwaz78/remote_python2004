
from django.urls import path, include
from rest_framework import routers
from api import views


router = routers.DefaultRouter()
router.register('posts', views.PostView)
router.register('users', views.UserView)
router.register('categories', views.CategoryView)


app_name = 'api'

urlpatterns = [
	path('', include(router.urls)),
]
