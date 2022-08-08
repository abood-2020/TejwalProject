# Generated by Django 4.0 on 2022-07-13 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0018_alter_popularquestion_answer'),
        ('place', '0036_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='city',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='country.city'),
        ),
    ]
