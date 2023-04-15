from django.urls import path
from . import views
from django.http import HttpResponse



urlpatterns = [

    path('auth/', views.AutorListVIew.as_view()),
    path('addbookclass/', views.addbookclass),
    path('delbookclass/', views.delbookclass),
    path('upbookclass/', views.updatebookclass),
    path('sebookclass/', views.selectbookclass),

    path('addbookinfo/', views.addbookinfo),
    path('delbookinfo/', views.delbookinfo),
    path('upbookinfo/', views.updatebookinfo),
    path('sebookinfo/', views.selectbookinfo),

]

handler404 = views.page_not_found
