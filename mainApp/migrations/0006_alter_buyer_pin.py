# Generated by Django 4.2.4 on 2023-08-18 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0005_buyer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="buyer",
            name="pin",
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
