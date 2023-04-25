# Generated by Django 4.1.7 on 2023-04-25 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='商品名称')),
                ('price', models.FloatField(default=20.0, verbose_name='商品价格')),
                ('weight', models.IntegerField(default=500, verbose_name='商品重量')),
                ('image', models.ImageField(default='upload/1.jpg', upload_to='upload/%Y/%m', verbose_name='商品图片')),
                ('isnew', models.BooleanField(default=False, verbose_name='是否新品')),
                ('detail', models.TextField(default='', verbose_name='商品详情')),
            ],
        ),
    ]
