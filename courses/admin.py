from django.contrib import admin
from .models import Course,Category,CourseRegister
# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(CourseRegister)