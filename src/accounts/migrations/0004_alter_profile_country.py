# Generated by Django 4.0 on 2022-02-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_profile_brithdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(choices=[('PS', 'PS'), ('JAD', 'الأردن'), ('EGY', 'مصر'), ('AUS', 'السعودية'), ('EUS', 'الامارات '), ('AJZ', 'الجزائر')], max_length=40),
        ),
    ]
