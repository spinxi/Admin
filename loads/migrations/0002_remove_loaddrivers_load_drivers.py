# Generated by Django 4.1.5 on 2023-03-14 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loaddrivers',
            name='load_drivers',
        ),
    ]
