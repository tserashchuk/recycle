# Generated by Django 3.2.4 on 2021-07-07 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0015_auto_20210707_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2021-07-07 13:37:53.544823', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2021-07-07 13:37:53.523653', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2021-07-07 13:37:53.545252', max_length=200, verbose_name='URL'),
        ),
    ]
