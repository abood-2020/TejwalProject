# Generated by Django 4.0 on 2022-07-25 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0055_rename_title_place_place_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='title',
        ),
        migrations.AddField(
            model_name='place',
            name='title_place',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]