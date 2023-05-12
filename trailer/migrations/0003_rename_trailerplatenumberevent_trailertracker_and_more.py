# Generated by Django 4.1.3 on 2022-12-08 16:01

from django.db import migrations
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pghistory', '0005_events_middlewareevents'),
        ('trailer', '0002_trailerplatenumberevent_trailer_snapshot_insert_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TrailerPlateNumberEvent',
            new_name='TrailerTracker',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='trailer',
            name='snapshot_insert',
        ),
        pgtrigger.migrations.RemoveTrigger(
            model_name='trailer',
            name='snapshot_update',
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='trailer',
            trigger=pgtrigger.compiler.Trigger(name='snapshot_insert', sql=pgtrigger.compiler.UpsertTriggerSql(func='INSERT INTO "trailer_trailertracker" ("pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "plate_number") VALUES (_pgh_attach_context(), NOW(), \'snapshot\', NEW."id", NEW."plate_number"); RETURN NULL;', hash='b2ba00f1668706f7cec06ad7e79629829e8ebed3', operation='INSERT', pgid='pgtrigger_snapshot_insert_1610a', table='trailer_trailer', when='AFTER')),
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='trailer',
            trigger=pgtrigger.compiler.Trigger(name='snapshot_update', sql=pgtrigger.compiler.UpsertTriggerSql(condition='WHEN (OLD."plate_number" IS DISTINCT FROM (NEW."plate_number"))', func='INSERT INTO "trailer_trailertracker" ("pgh_context_id", "pgh_created_at", "pgh_label", "pgh_obj_id", "plate_number") VALUES (_pgh_attach_context(), NOW(), \'snapshot\', NEW."id", NEW."plate_number"); RETURN NULL;', hash='97784c86ce809396f59b43926eafc29fdecad858', operation='UPDATE', pgid='pgtrigger_snapshot_update_02dc4', table='trailer_trailer', when='AFTER')),
        ),
    ]