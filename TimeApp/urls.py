from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('time_display/', views.style),
    path('time_actual/', views.js),
]