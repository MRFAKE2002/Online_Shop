# Generated by Django 5.0.1 on 2024-02-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_discount_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=1, verbose_name='inventory'),
            preserve_default=False,
        ),
    ]
