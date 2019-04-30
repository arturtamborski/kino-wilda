from django.urls import path

from backend.api import views

urlpatterns = [
    path('top/', views.top),
    path('movies/', views.movies),
    path('comments/', views.comments),
]
