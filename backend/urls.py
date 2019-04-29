from django.urls import path

from backend.api import views

urlpatterns = [
    path(r'^top/$', views.top),
    path(r'^movies/$', views.movies),
    path(r'^comments/$', views.comments),
]
