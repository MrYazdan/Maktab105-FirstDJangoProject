from django.urls import path
from . import views
urlpatterns = [
    path('music/', views.musicview)
]