# Generated by Django 4.2 on 2024-10-11 08:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("qianwenpro", "0003_goods"),
    ]

    operations = [
        migrations.AddField(
            model_name="cates",
            name="numbers",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
