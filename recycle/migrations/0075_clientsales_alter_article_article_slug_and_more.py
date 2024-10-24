# Generated by Django 5.1.1 on 2024-10-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0074_alter_article_article_slug_alter_category_cat_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientSales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('short_desc', models.TextField(blank=True, verbose_name='Описание')),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2024-10-22 13:53:57.511619', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2024-10-22 13:53:57.510618', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2024-10-22 13:53:57.510618', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2024-10-22 13:53:57.511619', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_slug',
            field=models.CharField(default='article2024-10-22 13:53:57.512618', max_length=200, verbose_name='URL'),
        ),
        migrations.AddField(
            model_name='client',
            name='sales',
            field=models.ManyToManyField(blank=True, to='recycle.clientsales'),
        ),
    ]