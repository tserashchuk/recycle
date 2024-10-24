# Generated by Django 3.2.4 on 2024-02-21 07:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0067_auto_20230610_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_name', models.CharField(max_length=200, verbose_name='Заголовок H1')),
                ('tweet_slug', models.CharField(default='article2024-02-21 10:44:49.473292', max_length=200, verbose_name='URL')),
                ('tweet_short_desc', models.TextField(blank=True, verbose_name='Короткое описание для Schema')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='region',
            name='region_add_info',
            field=models.TextField(blank=True, verbose_name='Доп. информация'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2024-02-21 10:44:49.471243', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2024-02-21 10:44:49.435497', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2024-02-21 10:44:49.470665', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='punkt',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='region',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2024-02-21 10:44:49.471729', max_length=200, verbose_name='URL'),
        ),
    ]
