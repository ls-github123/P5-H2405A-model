# Generated by Django 4.2 on 2024-09-21 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("qianwenpro", "0002_torders"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cates",
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
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("add_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Questions",
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
                ("ask", models.CharField(blank=True, max_length=50, null=True)),
                ("answer", models.CharField(blank=True, max_length=50, null=True)),
                ("add_time", models.DateTimeField(auto_now_add=True)),
                (
                    "cid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="questions",
                        to="qianwenpro.cates",
                    ),
                ),
            ],
        ),
    ]
