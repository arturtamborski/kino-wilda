from django.urls import path

from backend.api import views

urlpatterns = [
    path('top/', views.top, name='top'),
    path('movies/', views.Movie.as_view(), name='movies'),
    path('comments/', views.Comment.as_view(), name='comments'),
]
