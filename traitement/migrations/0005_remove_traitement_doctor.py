# Generated by Django 2.2.10 on 2020-07-11 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traitement', '0004_auto_20200711_1816'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='traitement',
            name='doctor',
        ),
    ]
