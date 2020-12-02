from django.urls import path
from backend import views

urlpatterns = [
    path('', views.login, name='login'),
    path('dashboard-page/', views.dashboard, name='dashboard'),
]
