# Generated by Django 4.0 on 2022-07-13 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0034_remove_place_actvity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='title_activity',
            new_name='title',
        ),
    ]
