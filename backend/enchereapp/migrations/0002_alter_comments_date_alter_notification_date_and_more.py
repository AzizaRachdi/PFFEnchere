# Generated by Django 4.0.6 on 2022-09-11 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enchereapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 10, 3, 34, 564339)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 10, 3, 34, 565338)),
        ),
        migrations.AlterField(
            model_name='offre',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 10, 3, 34, 562340)),
        ),
        migrations.AlterField(
            model_name='proposition',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 11, 10, 3, 34, 563339)),
        ),
    ]
