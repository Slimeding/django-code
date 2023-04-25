from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from goods.models import GoodsInfo

class GoodsListView(ListView):
    model=GoodsInfo
    template_name='goodslist.html'
    context_object_name='goods'

class detailview(DetailView):
    def get(self, request, goods_id):
        goods = GoodsInfo.objects.get(id=int(goods_id))
        return render(request, 'gooddetail.html', {'goods': goods})



