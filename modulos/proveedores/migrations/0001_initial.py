# Generated by Django 4.2.3 on 2023-07-23 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Proveedores",
            fields=[
                (
                    "proveedor_id",
                    models.CharField(max_length=20, primary_key=True, serialize=False),
                ),
                ("razon_social", models.CharField(max_length=100)),
                ("cuit", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("telefono", models.CharField(max_length=20)),
                ("mov", models.BooleanField(default=False)),
            ],
        ),
    ]