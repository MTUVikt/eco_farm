# Generated by Django 4.0.5 on 2022-06-21 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_item',
            field=models.ManyToManyField(to='shop.cartitem'),
        ),
    ]
