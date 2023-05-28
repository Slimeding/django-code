from django.contrib import admin
from goods.models import GoodsInfo
from django.utils.html import mark_safe

# Register your models here.

# class GoodInfoAdmin(admin.ModelAdmin):
#    def buttons(self, obj):
#        button_html = """<a class="changelink"
#        href="http://localhost:8000/admin/goods/goodsinfo/%s/change/">
#        编辑</a>""" %(obj.id)
#        return mark_safe(button_html)
# buttons.short_description = 'good'
#
# list_display = ('id', 'name','price', 'weight', 'image', 'isnew', 'detail')
# list_editable = ('price', 'weight')
# search_fields = ('name',)
#
# admin.site.register(GoodsInfo, GoodInfoAdmin)

class GoodInfoAdmin(admin.ModelAdmin):
   def buttons(self, obj):
       button_html = """ <a class="changelink" 
       href="http://127.0.0.1:8000/admin/goods/goodsinfo/%s/change/">
       编辑</a>""" %(obj.id)
       return mark_safe(button_html)
   buttons.short_description =" 操作 " # 将short_description属性设置为GoodInfoAdmin类的属性之一

   def goodimg(self, obj):
        goodimg_html = """<img src="%s" width="50px" />""" %(obj.image.url)
        return mark_safe(goodimg_html)
   list_display = ('id', 'name','price', 'weight', 'image', 'isnew', 'detail', 'buttons', 'goodimg')
   list_editable = ('price', 'weight')
   search_fields = ('name',)

admin.site.register(GoodsInfo, GoodInfoAdmin)
admin.site.site_header = '商品信息管理系统后台'
admin.site.site_title = '后台管理系统'
