# Generated by Django 4.1.3 on 2022-12-08 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trailer', '0003_rename_trailerplatenumberevent_trailertracker_and_more'),
    ]

    operations = [
        pgtrigger.migrations.RemoveTrigger(
            model_name='trailer',
            name='snapshot_insert',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='trailer',
            name='snapshot_update',
        ),
        migrations.AddField(
            model_name='trailertracker',
            name='updated_by',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='trailertracker',
            name='pgh_obj',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='updated_by_plate_number_event', to='trailer.trailer'),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='trailer',
            trigger=pgtrigger.compiler.Trigger(name='snapshot_insert', sql=pgtrigger.compiler.UpsertTriggerSql(func='INSERT INTO "trailer_trailertracker" ("pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "plate_number", "updated_by_id") VALUES (_pgh_attach_context(), NOW(), \'snapshot\', NEW."id", NEW."plate_number", NEW."updated_by_id"); RETURN NULL;', hash='16d30b9c822bd23811d66925855cad3bda90da2c', operation='INSERT', pgid='pgtrigger_snapshot_insert_1610a', table='trailer_trailer', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='trailer',
            trigger=pgtrigger.compiler.Trigger(name='snapshot_update', sql=pgtrigger.compiler.UpsertTriggerSql(condition='WHEN (OLD."updated_by_id" IS DISTINCT FROM (NEW."updated_by_id") OR OLD."plate_number" IS DISTINCT FROM (NEW."plate_number"))', func='INSERT INTO "trailer_trailertracker" ("pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "plate_number", "updated_by_id") VALUES (_pgh_attach_context(), NOW(), \'snapshot\', NEW."id", NEW."plate_number", NEW."updated_by_id"); RETURN NULL;', hash='45c299ccd19a1aa6452199db7d2c90104018c081', operation='UPDATE', pgid='pgtrigger_snapshot_update_02dc4', table='trailer_trailer', when='AFTER')),
        ),
    ]