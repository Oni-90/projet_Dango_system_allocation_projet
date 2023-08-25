from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group

# Create your models here.


class Utilisateur(AbstractUser):
    ROLE_CHOICES = (
        ('etudiant', 'Etudiant'),
        ('enseignant', 'Enseignant'),
        ('administrateur', 'Administrateur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default='Etudiant')
    date_naissance = models.DateField(null=True, blank=True)
    numero_etudiant_enseignant = models.CharField(max_length=20, unique=True, null=True, blank=True)

    groups = models.ManyToManyField(Group, related_name='users_milestone')
    user_permissions = models.ManyToManyField(
        Permission, related_name='users_milestone')
    def __str__(self):
        return self.username
