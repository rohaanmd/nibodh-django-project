# Generated by Django 3.2.6 on 2021-08-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]