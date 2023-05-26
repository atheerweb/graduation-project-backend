from django.urls import path
from .views import top_5_freelancers, get_freelancer_with_projects , get_random_users,get_freelancers
from .views import get_jobs


urlpatterns = [
    # other URLs
    path('all-freelancers/',  get_freelancers, name='all-freelancers'),
    path('top-5-freelancers/', top_5_freelancers, name='top-5-freelancers'),
    path('freelancer/<str:id>/', get_freelancer_with_projects, name='get-freelancer-with-projects'),
    path('get_random/', get_random_users, name='get_random_users'),
    path('jobs/',get_jobs, name='get_jobs'),

]
