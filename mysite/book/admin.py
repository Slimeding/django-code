from django.contrib import admin
from book.models import BookClass,BookInfo
from book.models import BookISBN,AutorInfo
# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    list_display=('id',"name")
class BookClassAdmin(admin.ModelAdmin):
    list_display=('id',"name")
class BookISBNAdmin(admin.ModelAdmin):
    list_display = ("id","isbn")
class AutorInfoAdmin(admin.ModelAdmin):
    list_display = ("id","name")


admin.site.register(BookClass,BookClassAdmin)
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(BookISBN,BookISBNAdmin)
admin.site.register(AutorInfo,AutorInfoAdmin)
admin.site.site_header="管理后台"
admin.site.site_title="后台管理系统"
