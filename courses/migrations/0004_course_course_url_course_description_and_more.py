# Generated by Django 4.2 on 2023-06-11 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_courseregister_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_url',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='image_url',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
