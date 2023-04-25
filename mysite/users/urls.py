from django.urls import path
from . import views
from django.http import HttpResponse




urlpatterns = [
    path('index/', views.index),
    # path('login/', views.login),
    # path('add/', views.add),
]
