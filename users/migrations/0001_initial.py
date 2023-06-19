# Generated by Django 4.2 on 2023-06-19 00:50

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('permission_id', models.AutoField(primary_key=True, serialize=False)),
                ('permission_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('role_id', models.AutoField(primary_key=True, serialize=False)),
                ('role_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
                ('user_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_name', models.CharField(max_length=255)),
                ('transaction_date', models.DateTimeField(default=datetime.datetime.now)),
                ('course_fore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('user_fore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RolePermetion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permeion_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.permission')),
                ('role_rel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.role')),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='role_to_per',
            field=models.ManyToManyField(through='users.RolePermetion', to='users.permission'),
        ),
    ]
