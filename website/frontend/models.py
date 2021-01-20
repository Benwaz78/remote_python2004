from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    age = models.PositiveIntegerField()
    website = models.URLField(blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    cat_desc = models.TextField(blank=True, null=True, verbose_name='Description')

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural='Post Category'


class Post(models.Model):
    FEATURE = 'Feature'
    NO_FEATURE = 'No Feature'
    CHOOSE = ''
    APEAR_HOME_FIELD=[
        (FEATURE, 'Appear on home'),
        (NO_FEATURE, "Don't show on home"),
        (CHOOSE, 'Please Choose')
    ]

    pst_title = models.CharField(max_length=150, verbose_name='Post Title')
    pst_image = models.ImageField(null=True, verbose_name='Post Image', blank=True, upload_to='uploads/')
    cat_id = models.ManyToManyField(Category, verbose_name='Category')
    appear_home = models.CharField(max_length=50, choices=APEAR_HOME_FIELD, default=CHOOSE)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pst_title

    class Meta():
        verbose_name_plural = 'Post'

    def post_img(self):
        if self.pst_image:
          return self.pst_image.url


class About(models.Model):
    name = models.CharField(max_length=150)
    profile = models.ImageField(blank=True, null=True, upload_to='uploads/')
    content = models.TextField()

    def __str__(self):
        return self.name

    def profile_img(self):
        if self.profile:
          return self.profile.url
        return '/media/uploads/avatar.png'

    class Meta():
        verbose_name_plural='About'


