from django.urls import path
from frontend import views

app_name = 'frontend'

urlpatterns = [
    path('', views.about, name='about'),
    path('contact-page/', views.contact, name='contact'),
]
