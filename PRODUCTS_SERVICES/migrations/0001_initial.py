# Generated by Django 5.0.4 on 2024-04-15 08:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("NAME", models.CharField(max_length=255)),
                ("SLUG", models.SlugField(max_length=255)),
                ("CREATED_AT", models.DateTimeField(auto_now_add=True)),
                ("UPDATED_AT", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="SERVICES",
            fields=[
                ("ID", models.AutoField(primary_key=True, serialize=False)),
                ("NAME", models.CharField(max_length=255)),
                ("SLUG", models.SlugField(max_length=255)),
                ("CREATED_AT", models.DateTimeField(auto_now_add=True)),
                ("UPDATED_AT", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
