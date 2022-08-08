# Generated by Django 4.0 on 2022-02-19 18:58

from django.db import migrations, models
import place.models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0011_remove_place_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.CharField(choices=[('sea_activity', 'أنشطة البحار'), ('adventures', ' مغامرات'), ('sport', ' رياضه'), ('family_activity', ' نشاط عائلي')], default=1, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(null=True, upload_to=place.models.upload_image_activity),
        ),
        migrations.AddField(
            model_name='activity',
            name='info',
            field=models.TextField(max_length=800, null=True),
        ),
    ]
