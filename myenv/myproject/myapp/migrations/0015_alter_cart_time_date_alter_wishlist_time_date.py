# Generated by Django 5.0.7 on 2024-11-29 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_cart_roundtotal_alter_cart_time_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='time_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 29, 15, 45, 52, 753872, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='time_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 29, 15, 45, 52, 753872, tzinfo=datetime.timezone.utc)),
        ),
    ]
