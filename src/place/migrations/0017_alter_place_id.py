# Generated by Django 4.0 on 2022-02-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0016_alter_place_background_alter_place_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
