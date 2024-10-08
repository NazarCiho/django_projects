from django.urls import path
from . import views

app_name = 'hello'

urlpatterns = [
    path('', views.index, name='index'),
    path('query/', views.say_hello_query, name='say_hello_query'),
    path('<str:name>/', views.say_hello_path, name='say_hello_path'),

]
