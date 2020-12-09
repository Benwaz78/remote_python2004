from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('detail/<int:abt_id>/', views.about_detail, name='about_detail'),
    path('post-list/', views.post_list, name='post_list'),
    path('contact-page/', views.contact, name='contact'),
]
