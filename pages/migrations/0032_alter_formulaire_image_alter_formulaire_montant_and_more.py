# Generated by Django 4.2 on 2023-04-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0031_alter_formulaire_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulaire",
            name="image",
            field=models.ImageField(null=True, upload_to="photos"),
        ),
        migrations.AlterField(
            model_name="formulaire",
            name="montant",
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="formulaire",
            name="nom",
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name="formulaire",
            name="prenom",
            field=models.CharField(max_length=25, null=True),
        ),
    ]
