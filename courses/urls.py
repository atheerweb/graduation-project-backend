from courses import views
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
router  = DefaultRouter()
router.register('Coures', views.viewsets_courses)

urlpatterns = [
    path('courses/', views.get_courses),
    path('top/', views.get_top5_courses),
    path('course/<int:id>/', views.get_course),
    path('category/', views.get_category),
    # viewsets courses url
    path('Viewsets/',include(router.urls)),

    # find by postman
    #path('Viewsets/Coures/find/', views.find_course),
]
