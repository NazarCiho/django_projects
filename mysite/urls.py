
from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
    path('', include('homeapp.urls')),
    path('calc/', include('calc.urls')),
    path('hello/', include('hello.urls')),
    path('guess_game/', include('guess_game.urls')),
]
