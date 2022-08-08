# Generated by Django 4.0 on 2022-02-15 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name_city', models.CharField(max_length=30)),
                ('info', models.TextField(max_length=500)),
                ('formal_lang', models.CharField(max_length=50)),
                ('area_country', models.DecimalField(decimal_places=2, max_digits=12)),
                ('slug', models.SlugField(blank=True)),
                ('order_city', models.IntegerField()),
                ('country', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='country.country')),
            ],
        ),
    ]
