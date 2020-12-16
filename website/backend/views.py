from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from backend.forms import *


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('backend:dashboard')
        else:
            messages.error(request, 'Username and Password do not match')
    return render(request, 'frontend/login.html')


@login_required(login_url='/dashboard/')
def dashboard(request):
    return render(request, 'backend/index.html')


@login_required(login_url='/dashboard/')
def confirm_logout(request):
    return render(request, 'backend/confirm-logout.html')


@login_required(login_url='/dashboard/')
def logout_view(request):
    logout(request)
    return redirect('backend:login_view')


def category_form(request):
    if request.method=='POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, 'Category created')
    else:
        category_form = CategoryForm()
    return render(request, 'backend/add-category.html', {'cat':category_form})


def register_form(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'User Register')
    else:
        register_form = RegisterForm()
    return render(request, 'frontend/register.html', {'reg': register_form})


def post_form(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'User Register')
    else:
        post_form = PostForm()
    return render(request, 'backend/add-post.html', {'post': post_form})

def show_post(request):
    list_post = Post.objects.order_by('-date')
    return render(request, 'backend/view-posts.html', {'list':list_post})


def delete_post(request, post_id):
    post_record = get_object_or_404(Post, id=post_id)
    post_record.delete()
    return redirect('backend:show_post')


def edit_post(request, post_id):
    single_post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, request.FILES, instance=single_post)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'User Register')
    else:
        post_form = PostForm(instance=single_post)
    return render(request, 'backend/add-post.html', {'post': post_form})
