# Generated by Django 4.2 on 2023-04-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0019_alter_formulaire_image_alter_formulaire_nom_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulaire",
            name="image",
            field=models.ImageField(blank=True, default=None, upload_to="photos"),
        ),
    ]