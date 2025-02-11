# Generated by Django 5.0.4 on 2024-04-15 08:18

import VACANCIES.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Jobs",
            fields=[
                ("Id", models.AutoField(primary_key=True, serialize=False)),
                ("Title", models.CharField(max_length=255)),
                ("Job_name", models.CharField(max_length=255)),
                ("Open_date", models.DateField()),
                ("Close_date", models.DateField()),
                ("Created_at", models.DateTimeField(auto_now_add=True)),
                ("Updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Candidates",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=255)),
                ("Email", models.EmailField(max_length=255)),
                ("Created_at", models.DateTimeField(auto_now_add=True)),
                ("CV", models.FileField(upload_to=VACANCIES.models.get_upload_path)),
                (
                    "Position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="VACANCIES.jobs"
                    ),
                ),
            ],
        ),
    ]
