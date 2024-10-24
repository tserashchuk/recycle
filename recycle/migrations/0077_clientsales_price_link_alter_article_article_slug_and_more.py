# Generated by Django 5.1.1 on 2024-10-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0076_remove_client_sales_alter_article_article_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsales',
            name='price_link',
            field=models.CharField(blank=True, max_length=200, verbose_name='Ссылка на специальный прайс'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_slug',
            field=models.CharField(default='article2024-10-22 15:41:33.881798', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_slug',
            field=models.CharField(default='slug2024-10-22 15:41:33.880799', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_slug',
            field=models.CharField(default='product2024-10-22 15:41:33.881798', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_slug',
            field=models.CharField(default='region2024-10-22 15:41:33.882798', max_length=200, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='tweet_slug',
            field=models.CharField(default='article2024-10-22 15:41:33.882798', max_length=200, verbose_name='URL'),
        ),
    ]
