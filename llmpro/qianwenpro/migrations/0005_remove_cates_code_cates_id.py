# Generated by Django 4.2 on 2024-09-21 01:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("qianwenpro", "0004_remove_cates_id_cates_code"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cates",
            name="code",
        ),
        migrations.AddField(
            model_name="cates",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=1,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]
