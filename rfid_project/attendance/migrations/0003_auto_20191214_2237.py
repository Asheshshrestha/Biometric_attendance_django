# Generated by Django 2.2.2 on 2019-12-14 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_auto_20191214_2235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mode_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose', models.CharField(max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 12, 14, 22, 37, 29, 472023)),
        ),
        migrations.AlterField(
            model_name='log',
            name='time_in',
            field=models.TimeField(default=datetime.datetime(2019, 12, 14, 22, 37, 29, 472023)),
        ),
    ]
