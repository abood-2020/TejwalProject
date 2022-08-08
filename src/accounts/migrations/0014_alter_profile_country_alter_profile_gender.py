# Generated by Django 4.0 on 2022-07-28 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_profile_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(choices=[('PS', 'PS'), ('JAD', 'الأردن'), ('EGY', 'مصر'), ('AUS', 'السعودية'), ('EUS', 'الامارات '), ('AJZ', 'الجزائر')], max_length=40),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('Male', 'ذكر'), ('Female', 'انثى')], max_length=10),
        ),
    ]
