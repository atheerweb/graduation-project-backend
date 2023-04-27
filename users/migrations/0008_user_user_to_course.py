# Generated by Django 4.2 on 2023-04-27 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_course_user_re_course_user_to_course'),
        ('users', '0007_remove_permission_permission_has_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_to_course',
            field=models.ManyToManyField(through='courses.CourseRegister', to='courses.course'),
        ),
    ]