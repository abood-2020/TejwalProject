# Generated by Django 4.0 on 2022-04-16 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0025_place_actvity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='category',
            field=models.CharField(choices=[('sea_activity', 'أنشطة البحار'), ('adventures', ' مغامرات'), ('sport', ' رياضه'), ('control', 'قياده وتحكم'), ('family_activity', ' نشاط عائلي')], max_length=80),
        ),
    ]
