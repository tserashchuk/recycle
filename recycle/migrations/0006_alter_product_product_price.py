# Generated by Django 3.2.4 on 2021-06-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0005_alter_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
    ]
