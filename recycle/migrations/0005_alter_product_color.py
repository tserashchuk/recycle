# Generated by Django 3.2.4 on 2021-06-30 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recycle', '0004_alter_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('kg', 'за кг'), ('cn', 'за шт')], default='kg', max_length=6, verbose_name='Оплата'),
        ),
    ]
