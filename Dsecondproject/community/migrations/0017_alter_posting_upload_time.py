# Generated by Django 4.0.4 on 2022-05-08 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0016_alter_posting_upload_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='upload_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 8, 19, 2, 39, 86733)),
        ),
    ]
