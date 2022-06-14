from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('/tutorial', views.Tutorial, name='tutorial'),
    path('/about', views.About, name='about'),
]