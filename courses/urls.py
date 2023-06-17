from courses import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
router  = DefaultRouter()
router.register('courses', views.viewsets_courses)

urlpatterns = [
    path('courses_fliter/', views.get_courses),
    path('category_fliter/', views.category_filter),
    path('top/', views.get_top5_courses),
    path('3-sug/', views.get_suggested_courses),
    path('course/<int:id>/', views.get_course),
    path('category/', views.get_category),
    # viewsets courses url
    path('viewsets/',include(router.urls)),
    path('course_url/<int:id>/', views.get_course_url),
    # find by postman
    #path('Viewsets/Coures/find/', views.find_course),
]
