# Generated by Django 4.2 on 2023-04-21 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlsparser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='xlsrow',
            name='operdate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
