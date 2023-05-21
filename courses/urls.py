from courses import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('courses/', views.get_category),
    path('top/', views.get_top5_courses),

]
