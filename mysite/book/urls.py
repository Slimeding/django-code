from django.urls import path
from . import views



urlpatterns = [
    path('autorlist/',views.AutorListView.as_view()),

    # path('addbookclass/', views.addbookclass),
    # path('delbookclass/', views.delbookclass),
    # path('updatebookclass', views.updatebookclass),
    # path('selectbookclass/', views.selectbookclass),
]
handler404=views.page_not_found