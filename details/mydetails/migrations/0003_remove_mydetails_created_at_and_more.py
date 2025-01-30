# Generated by Django 5.1.5 on 2025-01-30 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydetails', '0002_alter_mydetails_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mydetails',
            name='created_at',
        ),
        migrations.AddField(
            model_name='mydetails',
            name='current_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 30, 10, 12, 23, 666371, tzinfo=datetime.timezone.utc)),
        ),
    ]
