# Generated by Django 4.1.3 on 2022-11-15 05:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_wallpaper_wallpaper_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallpaper',
            name='wallpaper_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 11, 15, 11, 28, 19, 749133)),
        ),
    ]