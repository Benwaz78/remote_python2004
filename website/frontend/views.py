from django.shortcuts import render
from frontend.models import *
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags



from django.contrib import messages
# Create your views here.

def index(request):
    latest_post = Post.objects.order_by('-date')[:3]
    return render(request, 'frontend/index.html', {'latest':latest_post})

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

def post_from_cat(request, category_id):
    count_post = Post.objects.filter(cat_id__id=category_id).count()
    try:
        get_cat_name = Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        return render(request, 'frontend/404.html')
    get_cat_name = Category.objects.get(id=category_id)
    post_cat = Post.objects.filter(cat_id__id=category_id).order_by('-date')
    context = {'posts': post_cat, 'counts': count_post, 'cat': get_cat_name}
    return render(request, 'frontend/post-cat.html', context)

def single_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except ObjectDoesNotExist:
        return render(request, 'frontend/404.html')
    return render(request, 'frontend/single-blog.html', {'single':post})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phoneNo')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        referer = request.POST.get('referer')
        message = request.POST.get('message')
        subject = 'Contact Us Contact'
        context = {
            'name':name,
            'phone':phone,
            'email':email,
            'gender':gender,
            'referer':referer,
            'message': message
        }
        html_message = render_to_string('frontend/mail-template.html', context)
        plain_message = strip_tags(html_message)
        from_email = 'From <slimchibenedict@gmail.com>'
        send = mail.send_mail(subject, plain_message, from_email, [
                    'uwazie.benedict@alabiansolutions.com', 'nonwaz@yahoo.com'], html_message=html_message)
        if send:
            messages.success(request, 'Email sent')
        else:
            messages.error(request, 'Mail not sent')

    return render(request, 'frontend/contact.html')
