# Generated by Django 4.0 on 2022-04-16 05:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0026_alter_activity_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['order']},
        ),
    ]
