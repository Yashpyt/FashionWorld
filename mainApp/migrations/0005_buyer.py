# Generated by Django 4.2.4 on 2023-08-17 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0004_alter_product_stock"),
    ]

    operations = [
        migrations.CreateModel(
            name="Buyer",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=30)),
                ("username", models.CharField(max_length=30, unique=True)),
                ("email", models.EmailField(max_length=30)),
                ("address", models.TextField(blank=True, default="", null=True)),
                ("pin", models.IntegerField(blank=True, default="", null=True)),
                (
                    "city",
                    models.CharField(blank=True, default="", max_length=50, null=True),
                ),
                (
                    "state",
                    models.CharField(blank=True, default="", max_length=50, null=True),
                ),
                (
                    "pic",
                    models.ImageField(
                        blank=True, default="", null=True, upload_to="uploads/users"
                    ),
                ),
            ],
        ),
    ]
