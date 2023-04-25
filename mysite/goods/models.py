from django.db import models

# Create your models here.



class GoodsInfo(models.Model):
    name= models.CharField(max_length=30, verbose_name=u'商品名称')
    price= models.FloatField(verbose_name=u'商品价格', default=20.0)
    weight=models.IntegerField(verbose_name=u'商品重量', default=500)
    image=models.ImageField(upload_to='upload/%Y/%m', verbose_name=u'商品图片', default='upload/1.jpg')
    isnew=models.BooleanField(verbose_name=u'是否新品', default=False)
    detail=models.TextField(verbose_name=u'商品详情', default='')

    def __str__(self):
        return self.name
