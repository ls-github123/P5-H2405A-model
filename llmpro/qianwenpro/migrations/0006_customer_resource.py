# Generated by Django 4.2 on 2024-10-15 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("qianwenpro", "0005_cates_userid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=200)),
                ("password", models.CharField(max_length=200)),
                ("account", models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Resource",
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
                ("name", models.CharField(max_length=200, unique=True)),
                ("url", models.IntegerField()),
                (
                    "customer",
                    models.ManyToManyField(
                        related_name="resource", to="qianwenpro.customer"
                    ),
                ),
                (
                    "pid",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="qianwenpro.resource",
                    ),
                ),
            ],
        ),
    ]
