from django.urls import path
from . import views


urlpatterns = [
    path('addbookclass/', views.addbookclass),
    path('delbookclass/', views.delbookclass),
    path('updatebookclass', views.updatebookclass),
    path('selectbookclass/', views.selectbookclass),
]
