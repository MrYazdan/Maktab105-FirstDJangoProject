# music/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.MusicInfoView.as_view(), name='info'),
    path('Main/', views.MusicInfoView.as_view(), name='info'),
    path('add/', views.MusicAddView.as_view(), name='add'),
    path('info/', views.CountAllView.as_view(), name='Main'),
    path('delete/<int:pk>/', views.MusicDeleteView.as_view(), name='delete'),
    path('delete/<str:pk>/', views.MusicDeleteView.as_view(), name='delete'),
]
