# Generated by Django 4.2 on 2023-06-07 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_category_cat_has_courses_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregister',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
