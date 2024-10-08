from django.urls import path
from . import views

app_name = 'calc'

urlpatterns = [
    path('', views.index, name='index'),
    path('query/', views.calcquery, name='calcquery'),
    path('<int:a>/<int:b>/<str:diya>/', views.calculate_multiplication,name="calculate_multiplication"),
]