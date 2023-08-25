# Generated by Django 4.2.4 on 2023-08-24 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MilestoneUser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='date_naissance',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='numero_etudiant_enseignant',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='role',
            field=models.CharField(choices=[('etudiant', 'Etudiant'), ('enseignant', 'Enseignant'), ('administrateur', 'Administrateur')], default='Etudiant', max_length=20),
        ),
    ]