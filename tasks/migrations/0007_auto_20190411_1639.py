# Generated by Django 2.0.13 on 2019-04-11 16:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20190410_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='done_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 11, 16, 39, 44, 629588, tzinfo=utc), editable=False),
        ),
    ]