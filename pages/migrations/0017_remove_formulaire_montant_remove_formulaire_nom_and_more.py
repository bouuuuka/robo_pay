# Generated by Django 4.2 on 2023-04-12 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0016_alter_formulaire_montant"),
    ]

    operations = [
        migrations.RemoveField(model_name="formulaire", name="montant",),
        migrations.RemoveField(model_name="formulaire", name="nom",),
        migrations.RemoveField(model_name="formulaire", name="prenom",),
    ]
