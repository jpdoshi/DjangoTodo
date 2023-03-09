# Generated by Django 4.1.7 on 2023-03-09 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0007_alter_todoitem_todo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='todo_time',
            field=models.TimeField(default=datetime.datetime(2023, 3, 9, 12, 54, 22, 19135, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='todo_title',
            field=models.CharField(max_length=50),
        ),
    ]