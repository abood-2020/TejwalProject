# Generated by Django 4.0 on 2022-02-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0004_alter_place_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
