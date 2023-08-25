# forms.py
from django import forms
from .models import Utilisateur
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class InscriptionForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ('username', 'password1', 'password2', 'role', 'date_naissance', 'numero_etudiant_enseignant')

class ConnexionForm(AuthenticationForm):
    class Meta:
        model = Utilisateur
