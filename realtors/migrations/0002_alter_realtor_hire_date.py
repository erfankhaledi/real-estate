# Generated by Django 4.2.2 on 2023-06-27 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 27, 10, 59, 57, 474402)),
        ),
    ]
