from django.shortcuts import render
from frontend.models import *
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'frontend/index.html')

def about(request):
    about = About.objects.all()
    user_var = User.objects.order_by('-last_name')
    context = {'abt':about, 'user':user_var}
    return render(request, 'frontend/about.html', context)

def about_detail(request, abt_id):
    detail = About.objects.get(id=abt_id)
    return render(request, 'frontend/detail.html', {'det':detail})

def post_list(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'frontend/post-list.html', {'pst':posts})

def contact(request):
    return render(request, 'frontend/contact.html')
