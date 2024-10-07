# simulation/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('simulate/', views.simulate, name='simulate'),
    path('update-distance/', views.update_distance, name='update_distance'),
    path('notification/', views.notification, name='notification'),
    path('challan/', views.challan, name='challan'),
]
