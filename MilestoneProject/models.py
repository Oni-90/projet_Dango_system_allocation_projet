from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

# models.py

from django.db import models

class Projet(models.Model):
    STATUT_CHOICES = (
        ('en_cours', 'En cours'),
        ('soumis', 'Soumis'),
        ('corrigé', 'Corrigé'),
        ('traité', 'Traité'),
        ('archivé', 'Archivé'),
    )

    intitule = models.CharField(max_length=100)
    matiere = models.CharField(max_length=100)
    fichier_projet = models.FileField(upload_to='projets/')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_cours')
   

class ChargerProjetEtudiant(models.Model):
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE)
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    fichier_traite = models.FileField(upload_to='soumissions_projet_etudiant/')
    date_soumission = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ChargerProjetEtudiant - Projet: {self.projet.intitule}, Fichier Traité: {self.fichier_traite}"



# class ProjetPrecedent(models.Model):
#     # Champs similaires à ceux du modèle Projet actuel
#     intitule = models.CharField(max_length=255)
#     matiere = models.CharField(max_length=100)
#     fichier_projet = models.FileField(upload_to='projets_precedents/')
#     statut = models.CharField(max_length=20, default='archivé')
#     date_creation = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.intitule