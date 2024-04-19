# Generated by Django 5.0.4 on 2024-04-19 04:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "WEBSITE",
            "0005_contactinfo_facebook_link_contactinfo_instagram_link_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="contactinfo",
            name="Facebook_link",
            field=models.CharField(default="www.facebook.com", max_length=255),
        ),
        migrations.AlterField(
            model_name="contactinfo",
            name="Instagram_link",
            field=models.CharField(default="www.instagram.com", max_length=255),
        ),
        migrations.AlterField(
            model_name="contactinfo",
            name="Latitude_Logitude",
            field=models.CharField(
                help_text="Right click on the google maps to get latitude and longitude",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="contactinfo",
            name="Linkedin_link",
            field=models.CharField(default="www.linkedin.com", max_length=255),
        ),
        migrations.AlterField(
            model_name="contactinfo",
            name="X_link",
            field=models.CharField(default="www.twitter.com", max_length=255),
        ),
        migrations.AlterField(
            model_name="contactinfo",
            name="Youtube_link",
            field=models.CharField(default="www.youtube.com", max_length=255),
        ),
    ]
