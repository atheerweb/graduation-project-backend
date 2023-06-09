# Generated by Django 4.2 on 2023-06-19 14:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='user_to_role',
            field=models.ManyToManyField(related_name='role_to_user', through='users.UserRoles', to=settings.AUTH_USER_MODEL),
        ),
    ]
