# Generated by Django 4.0 on 2022-07-13 09:16

from django.db import migrations, models
import django.db.models.deletion
import place.models


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0018_alter_popularquestion_answer'),
        ('place', '0035_rename_title_activity_activity_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=100)),
                ('audience', models.CharField(max_length=100)),
                ('info', models.TextField(max_length=500)),
                ('fees', models.BooleanField(default=False)),
                ('link_ticket', models.URLField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('background', models.ImageField(upload_to=place.models.upload_image_event)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.city')),
            ],
        ),
    ]