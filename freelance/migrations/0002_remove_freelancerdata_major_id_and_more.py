# Generated by Django 4.2 on 2023-06-07 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freelancerdata',
            name='major_id',
        ),
        migrations.AddField(
            model_name='freelancerdata',
            name='major_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Major',
        ),
    ]
