from django.urls import path
from . import views


urlpatterns = [
    path('addbookclass/', views.addbookclass),
    path('delbookclass/', views.delbookclass),
    path('upbookclass/', views.updatebookclass),
    path('sebookclass/', views.selectbookclass),
]
