# Generated by Django 4.2 on 2023-05-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_courseregister_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseregister',
            name='owner',
            field=models.BooleanField(default=False),
        ),
    ]
