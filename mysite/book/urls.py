from django.urls import path
from . import views




urlpatterns = [
    path('autorlist/',views.AutorListView.as_view()),

    path('addbookclass/', views.addbookclass),
    path('delbookclass/', views.delbookclass),
    path('updatebookclass', views.updatebookclass),
    path('selectbookclass/', views.selectbookclass),

    path('addbook/', views.addbook),
    path('delbook/', views.delbook),
    path('updatebook/', views.updatebook),
    path('selectbook/', views.selectbook),
]
handler404=views.page_not_found