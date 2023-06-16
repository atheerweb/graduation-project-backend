from django.urls import path , include
from .views import top_5_freelancers, get_freelancer_with_projects , get_random_users,get_freelancers
from .views import get_jobs,get_job,post,viewsets_job , viewsets_project
from freelance import views

from rest_framework.routers import DefaultRouter
router  = DefaultRouter()
router.register('job', views.viewsets_job)
router.register('project', views.viewsets_project)




urlpatterns = [
    # other URLs
    path('all-freelancers/',  get_freelancers, name='all-freelancers'),
    path('top-5-freelancers/', top_5_freelancers, name='top-5-freelancers'),
    path('freelancer/<str:id>/', get_freelancer_with_projects, name='get-freelancer-with-projects'),
    path('get_random/', get_random_users, name='get_random_users'),
    path('jobs/',get_jobs, name='get_jobs'),
    path('job/<str:id>',get_job, name='get_job'),
    path('post_job', post),
    path('viewsets/',include(router.urls)),

]
