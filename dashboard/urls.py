from django.urls import path, include
from . import views

# app_name = 'login'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout, name='logout'),
    path("", include("complaintbox.urls")),

]
