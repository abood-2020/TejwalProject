# Generated by Django 4.0 on 2022-03-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_plansplaces'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='tour_type',
            field=models.CharField(choices=[('worship', 'عبادة '), ('romantic tourism', 'قضاء شهر العسل'), ('family', 'عائلتي'), ('friends', 'أصدقائي'), ('Safari', 'سفاري'), ('medical', 'علاجية')], default='', max_length=30),
            preserve_default=False,
        ),
    ]
