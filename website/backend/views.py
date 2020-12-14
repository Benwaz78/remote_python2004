from django.shortcuts import render, redirect
# Create your views here.

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


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
