# Generated by Django 3.2.23 on 2024-02-10 06:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0007_auto_20240210_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='checkin_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 6, 15, 12, 260029, tzinfo=utc), verbose_name='check in time'),
        ),
        migrations.AlterField(
            model_name='work',
            name='checkout_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 10, 6, 15, 12, 260029, tzinfo=utc), verbose_name='check out time'),
        ),
    ]
