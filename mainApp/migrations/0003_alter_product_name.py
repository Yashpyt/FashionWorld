# Generated by Django 4.2.4 on 2023-08-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainApp", "0002_alter_brand_name_alter_maincategory_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=30),
        ),
    ]
