from django.urls import path

from . import views

urlpatterns = [
    path('quote', views.get_quotes, name='get_quotes'),
]