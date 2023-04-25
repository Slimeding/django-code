from django.urls import path, re_path
from . import views
import re


urlpatterns = [
    path('goodslist/', views.GoodsListView.as_view()),
   re_path(r'^gooddetail/(?P<goods_id>\d+)/$', views.detailview.as_view(),name='gooddetail'),
]




