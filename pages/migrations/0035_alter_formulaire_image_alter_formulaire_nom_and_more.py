# Generated by Django 4.2 on 2023-04-12 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0034_alter_formulaire_montant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulaire",
            name="image",
            field=models.ImageField(default=None, null=True, upload_to="photos"),
        ),
        migrations.AlterField(
            model_name="formulaire",
            name="nom",
            field=models.CharField(default="", max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name="formulaire",
            name="prenom",
            field=models.CharField(default="", max_length=25, null=True),
        ),
    ]