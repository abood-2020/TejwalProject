# Generated by Django 4.0 on 2022-07-26 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0021_food'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]