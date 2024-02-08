# Generated by Django 5.0.2 on 2024-02-08 19:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Rooms", "0003_remove_settings_roomsettings_remove_room_setup_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="topic",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="Rooms.topic",
            ),
        ),
    ]
