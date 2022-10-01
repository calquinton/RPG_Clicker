from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='game_home'),
    path('achievements/', views.achievements, name='game_achievements'),
]