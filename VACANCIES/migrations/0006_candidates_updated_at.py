# Generated by Django 5.0.4 on 2024-04-19 06:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("VACANCIES", "0005_candidates_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidates",
            name="Updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
