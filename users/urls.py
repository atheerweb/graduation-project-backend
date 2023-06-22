from django.urls import path
from . import views
from .views import get_user
urlpatterns = [
    path('role/<str:role>', views.role_list),
    path('ur/', views.UserRoles_list),
path('user/<str:id>/', get_user, name='get_user'),
    #path('ur/<slug:slug>/', views.role_list)
]
