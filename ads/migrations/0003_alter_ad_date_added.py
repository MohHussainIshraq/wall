# Generated by Django 5.0 on 2023-12-29 03:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ad_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]