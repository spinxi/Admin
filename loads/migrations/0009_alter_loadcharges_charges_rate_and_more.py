# Generated by Django 4.1.5 on 2023-05-02 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0008_alter_loaddelivery_load_alter_loadpickup_load_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadcharges',
            name='charges_rate',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='loadcharges',
            name='load',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='loadcharges', to='loads.loads'),
        ),
        migrations.AlterField(
            model_name='loaddelivery',
            name='load',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='loaddelivery', to='loads.loads'),
        ),
        migrations.AlterField(
            model_name='loadpickup',
            name='load',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='loadpickup', to='loads.loads'),
        ),
    ]
