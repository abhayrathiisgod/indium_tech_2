# Generated by Django 5.0.4 on 2024-04-19 05:54

import ckeditor.fields
import django.utils.timezone
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("VACANCIES", "0002_jobs_is_published"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobs",
            name="About_Role",
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="jobs",
            name="Job_Requirement",
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
