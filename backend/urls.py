from django.urls import path

from backend.api import views

urlpatterns = [
    path('top/', views.top),
    path('movies/', views.Movie.as_view()),
    path('comments/', views.Comment.as_view()),
]
