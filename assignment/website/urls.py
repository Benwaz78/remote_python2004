from django.urls import path
from website import views

app_name='website'

urlpatterns = [
    path('', views.about, name='about'),
    path('contact-page/', views.contact, name='contact'),
]
