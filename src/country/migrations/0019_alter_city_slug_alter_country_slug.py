# Generated by Django 4.0 on 2022-07-15 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0018_alter_popularquestion_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
