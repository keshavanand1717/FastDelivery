# Generated by Django 4.2.1 on 2023-06-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_creaated_at_job_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='pickup_address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_lat',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_lng',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='job',
            name='pickup_phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]