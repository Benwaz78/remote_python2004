from frontend.models import *
import datetime


def cat_menu(request):
    category = Category.objects.all()
    return {'category': category}

def footer_date(request):
    footer = datetime.datetime.now()
    return {'foot':footer}
