# Generated by Django 4.2 on 2023-04-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0030_alter_formulaire_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulaire",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="photos"),
        ),
    ]
