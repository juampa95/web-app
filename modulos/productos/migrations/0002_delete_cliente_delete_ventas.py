# Generated by Django 4.2.3 on 2023-07-23 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Cliente",
        ),
        migrations.DeleteModel(
            name="Ventas",
        ),
    ]
