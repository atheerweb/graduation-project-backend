from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list),
    path('role/<str:role>', views.role_list),
    path('ur/', views.UserRoles_list),
    #path('ur/<slug:slug>/', views.role_list)
]
