# Generated by Django 4.0 on 2022-03-14 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0024_remove_favorite_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='actvity',
            field=models.ManyToManyField(to='place.Activity'),
        ),
    ]
