from django.db import models
from accounts.models import MyUser
# Create your models here.


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.DecimalField(max_digits=10, decimal_places=2)
    user_to_course= models.ManyToManyField('accounts.MyUser',through='CourseRegister')
    def __str__(self):
        return str(self.course_id)


class Category(models.Model):
    category_name = models.CharField(max_length=255)
    cat_has_courses = models.ForeignKey(Course,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.category_name)
    
class CourseRegister(models.Model):
    user_rel = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    rating = models.IntegerField(unique= True)
    Course_rel = models.ForeignKey(Course, on_delete=models.CASCADE)
