# Generated by Django 4.2.1 on 2024-02-29 22:17

import bcs.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bcs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cow',
            name='picture',
            field=models.ImageField(blank=True, upload_to=bcs.models.upload_to),
        ),
    ]
