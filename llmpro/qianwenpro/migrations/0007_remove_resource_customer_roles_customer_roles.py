# Generated by Django 4.2 on 2024-10-16 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("qianwenpro", "0006_customer_resource"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="resource",
            name="customer",
        ),
        migrations.CreateModel(
            name="Roles",
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
                ("resources", models.ManyToManyField(to="qianwenpro.resource")),
            ],
        ),
        migrations.AddField(
            model_name="customer",
            name="roles",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="qianwenpro.roles",
            ),
        ),
    ]
