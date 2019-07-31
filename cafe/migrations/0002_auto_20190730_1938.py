# Generated by Django 2.2.1 on 2019-07-30 14:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cart_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 30, 19, 38, 53, 824927)),
        ),
        migrations.AddField(
            model_name='cart',
            name='emp_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='snack_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.FloatField(null=True),
        ),
    ]
