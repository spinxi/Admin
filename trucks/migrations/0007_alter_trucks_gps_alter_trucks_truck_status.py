# Generated by Django 4.1.3 on 2022-12-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trucks', '0006_alter_trucks_rent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trucks',
            name='gps',
            field=models.CharField(choices=[('Azuga', 'Azuga'), ('Verizon', 'Verizon')], default='Azuga', max_length=50),
        ),
        migrations.AlterField(
            model_name='trucks',
            name='truck_status',
            field=models.CharField(choices=[('Owner-Operator', 'Owner-Operator'), ('GA', 'GA'), ('Self Dot', 'Self Dot')], default='Owner-Operator', max_length=50),
        ),
    ]