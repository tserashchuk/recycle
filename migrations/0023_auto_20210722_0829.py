# Generated by Django 3.2.4 on 2021-07-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0022_auto_20210722_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2021-07-22 08:29:45.038056', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(default='IMG_4280_копия.jpg', upload_to='', verbose_name='Изображение категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2021-07-22 08:29:45.016826', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2021-07-22 08:29:45.038505', max_length=200, verbose_name='URL'),
        ),
    ]