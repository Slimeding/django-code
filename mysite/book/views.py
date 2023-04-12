from django.shortcuts import render
from django.http import HttpResponse
from .models import BookClass
from .models import BookInfo
from .models import BookISBN
from .models import AutorInfo
from django.views.generic.list import ListView



# Create your views here.

# 1.增加图书信息
def addbook(request):
    obj=BookInfo(name="python",price=100,autor="李四",desc="python是一门很好的语言",ishot=True)
    result=obj.save(obj)
    return HttpResponse("增加成功")

# 2.删除图书信息
def delbook(request):
    bookname=BookInfo.objects.filter(name="python")
    if not bookname:
        return HttpResponse("图书不存在")
    else:
        bookname.delete()
        return HttpResponse("删除成功")

# 3.修改图书信息
def updatebook(request):
    bookname=BookInfo.objects.filter(name="python")
    if not bookname:
        return HttpResponse("图书不存在")
    else:
        bookname.update(name="java")
        return HttpResponse("修改成功")

# 4.查询图书信息
def selectbook(request):
    bookname=BookInfo.objects.filter(name="java")
    if not bookname:
        return HttpResponse("图书不存在")
    else:
        return HttpResponse("查询成功")


# 1.增加图书信息
def addbookclass(request):
    obj=BookClass(name="文学类")
    result=obj.save(obj)
    return HttpResponse("增加成功")

# 2.删除图书信息
def delbookclass(request):
    classname=BookClass.objects.filter(name="文学类")
    if not classname:
        return HttpResponse("图书类别不存在")
    else:
        classname.delete()
        return HttpResponse("删除成功")


# 3.修改图书信息
def updatebookclass(request):
    classname=BookClass.objects.filter(name="文学类")
    if not classname:
        return HttpResponse("图书类别不存在")
    else:
        classname.update(name="历史类")
        return HttpResponse("修改成功")

# 4.查询图书信息
def selectbookclass(request):
    classname=BookClass.objects.filter(name="历史类")
    if not classname:
        return HttpResponse("图书类别不存在")
    else:
        return HttpResponse("查询成功")


class AutorListView(ListView):
    model = AutorInfo
    template_name = "list.html"
    context_object_name = 'my_autor'
#
#

def page_not_found(request,exception):
    return render(request,'404.html')