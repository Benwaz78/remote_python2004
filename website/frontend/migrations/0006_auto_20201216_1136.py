# Generated by Django 3.1.1 on 2020-12-16 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_post_appear_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='appear_home',
            field=models.CharField(choices=[('Feature', 'Appear on home'), ('No Feature', "Don't show on home"), ('', 'Please Choose')], default='', max_length=50),
        ),
    ]