# Generated by Django 4.2.1 on 2023-06-07 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_job'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='creaated_at',
            new_name='created_at',
        ),
    ]
