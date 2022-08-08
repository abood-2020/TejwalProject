# Generated by Django 4.0 on 2022-07-21 12:06

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0049_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='audience',
            field=models.CharField(choices=[('public', 'عام'), ('private', 'خاص')], max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('religious', 'ديني'), ('sport', 'الرياضه'), ('art', 'فن وثقافة'), ('festival', 'مهرجانات'), ('entertainment', 'ترفيه'), ('gallery', 'معارض'), ('conspiracy', 'مؤتمرات'), ('marketing', 'التسوق')], max_length=50),
        ),
        migrations.AlterField(
            model_name='place',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('families', 'مناسب للعائلات'), ('Children', 'مناسب للأطفال'), ('couples', 'مناسب للأطفال'), ('groups', 'مناسب للمجموعات'), ('Internet', 'إنترنت مجاني'), ('free', ' مجاني'), ('delivery', 'توصيل '), ('parking', ' موقف سيارات متاح'), ('Indoor_yards', 'ساحات داخليه '), ('outdoor_yards', 'ساحات خارجيه'), ('green_yards', 'ساحات خضراء')], max_length=102),
        ),
    ]