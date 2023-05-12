# Generated by Django 4.1.5 on 2023-01-31 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0004_driver_license_class_driver_license_exp_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='occ_cancel_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='occ_member_number',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='occ_start_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
    ]