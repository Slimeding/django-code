from django.db import models
from django.conf import settings


class BookClass(models.Model):
    name=models.CharField(max_length=20,verbose_name=u"图书类别")
    def __str__(self):
        return self.name

# class BookISBN(models.Model):
#     isbn=models.CharField(max_length=50,verbose_name=u"图书ISBN")
#     def __str__(self):
#         return self.isbn
#
#
# class AutorInfo(models.Model):
#     id=models.CharField(max_length=30, verbose_name=u"身份证号", primary_key=True)
#     name=models.CharField(max_length=20, verbose_name=u"姓名")
#     telephone = models.CharField(max_length=20, verbose_name=u"联系方式")
#     age = models.IntegerField(verbose_name=u"年龄", default=30)
#     sex = models.CharField(max_length=20, verbose_name=u"性别", default="男")
#     def __str__(self):
#         return self.name



class BookInfo(models.Model):
    # bookisbn=models.OneToOneField(BookISBN,on_delete=models.CASCADE)
    # autorinfo=models.ManyToManyField(AutorInfo)

    bookclass=models.ForeignKey(BookClass,on_delete=models.CASCADE,
                                verbose_name=u"图书类别",null=True,blank=True)
    name=models.CharField(max_length=30,verbose_name=u"图书名称")
    price=models.IntegerField(verbose_name=u"价格",default=20)
    autor=models.CharField(max_length=20,verbose_name=u"作者",default=" ")

    # desc = models.TextField(verbose_name=u"图书简介",default=" ")
    # image= models.ImageField(upload_to="upload/%Y/%m", verbose_name=u"图书封面", default="upload/default.png")
    #
    # ishot = models.BooleanField(verbose_name=u"是否畅销", default=False)
    # moredesc = models.TextField(verbose_name=u"更多介绍", default=" ")
    def __str__(self):
        return self.name









