# Generated by Django 4.2.1 on 2023-06-27 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_job_delivery_address_job_delivery_lat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='delivery_lat',
        ),
        migrations.RemoveField(
            model_name='job',
            name='delivery_lng',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pickup_lat',
        ),
        migrations.RemoveField(
            model_name='job',
            name='pickup_lng',
        ),
    ]
