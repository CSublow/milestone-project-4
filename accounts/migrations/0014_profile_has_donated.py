# Generated by Django 2.0.13 on 2019-05-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20190420_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='has_donated',
            field=models.BooleanField(default=False),
        ),
    ]