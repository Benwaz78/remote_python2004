from django.urls import path
from backend import views


app_name = 'backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('dashboard-page/', views.dashboard, name='dashboard'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('logout/', views.logout_view, name='logout_view'),
]
