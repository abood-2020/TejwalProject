# Generated by Django 4.0 on 2022-07-13 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0038_alter_activity_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='alert',
        ),
    ]
