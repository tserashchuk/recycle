# Generated by Django 3.2.4 on 2021-07-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0021_auto_20210722_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2021-07-22 08:21:29.275312', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение категории'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2021-07-22 08:21:29.252823', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2021-07-22 08:21:29.275737', max_length=200, verbose_name='URL'),
        ),
    ]
