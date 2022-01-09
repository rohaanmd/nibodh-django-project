# Generated by Django 3.2.6 on 2021-08-27 06:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='shop\\images'),
        ),
        migrations.AddField(
            model_name='course',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 27, 6, 18, 59, 251003, tzinfo=utc)),
        ),
    ]
