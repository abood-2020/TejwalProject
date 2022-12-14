# Generated by Django 4.0 on 2022-07-16 11:50

import country.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0020_country_meta_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title_food', models.CharField(max_length=50)),
                ('info', models.TextField(max_length=800)),
                ('category', models.CharField(choices=[('meat', 'لحوم'), ('vegetarian', 'مأكولات نباتية'), ('Seafood', 'وجبات بحرية'), ('Candy', 'حلويات'), ('fastfood', 'وجبات سريعة'), ('fastfood2', 'بقوليات'), ('fastfood3', 'وجبات')], max_length=30)),
                ('image', models.ImageField(upload_to=country.models.upload_food)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='country.country')),
            ],
        ),
    ]
