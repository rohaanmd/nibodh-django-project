# Generated by Django 3.2.6 on 2021-08-31 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartJson', models.CharField(max_length=200)),
                ('email', models.CharField(default='', max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('isSameBillingAddress', models.BooleanField()),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=200)),
                ('zip', models.IntegerField()),
            ],
        ),
    ]
