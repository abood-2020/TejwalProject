# Generated by Django 4.0 on 2022-07-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0019_alter_city_slug_alter_country_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='meta_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]