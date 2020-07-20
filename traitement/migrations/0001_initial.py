# Generated by Django 2.2.10 on 2020-06-01 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Traitement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.PositiveIntegerField(default=0)),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('traitement_content', models.CharField(default='', max_length=500)),
                ('traitement_title', models.CharField(default='', max_length=500)),
                ('traitement_type', models.CharField(default='', max_length=500)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
