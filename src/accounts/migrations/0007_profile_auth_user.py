# Generated by Django 4.0 on 2022-03-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_profile_person_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='auth_user',
            field=models.IntegerField(default=0),
        ),
    ]
