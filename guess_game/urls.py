from django.urls import path
from . import views

app_name = 'guess_game'

urlpatterns = [
    path('getform/', views.getform),
    path('', views.index, name='index'),
]