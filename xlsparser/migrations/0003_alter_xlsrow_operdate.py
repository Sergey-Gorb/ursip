# Generated by Django 4.2 on 2023-04-22 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xlsparser', '0002_xlsrow_operdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xlsrow',
            name='operdate',
            field=models.DateField(null=True),
        ),
    ]
