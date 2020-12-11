from django.shortcuts import render
# Create your views here.

def login_view(request):
    return render(request, 'frontend/login.html')


def dashboard(request):
    return render(request, 'backend/index.html')