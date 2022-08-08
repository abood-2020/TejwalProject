# Generated by Django 4.0 on 2022-04-23 10:07

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0031_place_relevance_alter_activity_alert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='relevance',
        ),
        migrations.AddField(
            model_name='place',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('families', 'مناسب للعائلات'), ('Children', 'مناسب للأطفال'), ('groups', 'مناسب للمجموعات'), ('Internet', 'إنترنت مجاني'), ('delivery', 'توصيل '), ('parking', ' موقف سيارات متاح'), ('Indoor_yards', 'ساحات داخليه '), ('outdoor_yards', 'ساحات خارجيه'), ('green_yards', 'ساحات خضراء')], default='', max_length=89),
            preserve_default=False,
        ),
    ]