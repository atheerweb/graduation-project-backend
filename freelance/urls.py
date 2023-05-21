
from django.urls import path
from freelance import views

urlpatterns = [

    path('jobs/', views.get_jops)

]
