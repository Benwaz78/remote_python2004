from django.urls import path
from backend import views


app_name = 'backend'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('dashboard-page/', views.dashboard, name='dashboard'),
    path('confirm-logout/', views.confirm_logout, name='confirm_logout'),
    path('logout/', views.logout_view, name='logout_view'),
    path('category/', views.category_form, name='category_form'),
    path('register-form/', views.register_form, name='register_form'),
    path('post-form/', views.post_form, name='post_form'),
    path('show-post/', views.show_post, name='show_post'),
    path('delete-post/<int:post_id>', views.delete_post, name='delete_post'),
    path('edit-post/<int:post_id>', views.edit_post, name='edit_post'),
    path('list-user-post/', views.ListPost.as_view(), name='user_post'),
    path('add-post/', views.AddPost.as_view(), name='add_post'),
]
