from django.urls import path , include
from .views import top_5_freelancers, get_freelancer_with_projects , get_random_users,get_freelancers
from .views import get_jobs,get_job,post,viewsets_job , viewsets_project , job_filter, freelancer_filter, freelancer_major_filter ,major_filter,get_all_major
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
    path('job/<int:id>',get_job, name='get_job'),
    path('post_job', post),
    path('viewsets/',include(router.urls)),
    path('filter_major/', views.major_filter),
    path('filter_job_name/', views.job_filter),
    path('filter_freelancer_name/', views.freelancer_filter),
    path('filter_freelancer_major/', views.freelancer_major_filter),
    path('all-majors/',  get_all_major, name='all-majors'),

]
