# Generated by Django 4.0 on 2022-07-20 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partspost',
            name='alt_image',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='source',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
