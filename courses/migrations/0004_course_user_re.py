# Generated by Django 4.2 on 2023-04-26 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_permission_permission_has_role_and_more'),
        ('courses', '0003_remove_course_user_re'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user_re',
            field=models.ManyToManyField(null=True, to='users.user'),
        ),
    ]
