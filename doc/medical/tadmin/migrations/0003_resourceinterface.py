# Generated by Django 5.0.6 on 2024-07-25 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tadmin", "0002_resource_roles_adminuser"),
    ]

    operations = [
        migrations.CreateModel(
            name="ResourceInterface",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.CharField(max_length=100)),
                (
                    "resid",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tadmin.resource",
                    ),
                ),
            ],
            options={
                "verbose_name": "接口权限表",
                "verbose_name_plural": "接口权限表",
                "db_table": "resource_interface",
            },
        ),
    ]
