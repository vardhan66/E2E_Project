from django.urls import path
from . import views

# app_name = 'login'
urlpatterns = [
    path('complain/', views.register_complant, name='complaint'),
]
