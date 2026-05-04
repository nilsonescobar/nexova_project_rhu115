from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('empleados/', views.empleados, name='empleados'),
    path('prestaciones/', views.prestaciones, name='prestaciones'),
    path('ausencias/', views.ausencias, name='ausencias'),
]