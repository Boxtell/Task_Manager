# Generated by Django 2.1.8 on 2019-05-16 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_auto_20190516_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasklist',
            name='my_tasks',
        ),
    ]
