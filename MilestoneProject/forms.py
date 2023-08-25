from django import forms
from .models import ChargerProjetEtudiant
from MilestoneProject.models import Projet

class ProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['intitule', 'matiere', 'fichier_projet', 'statut']



class ChargerProjetEtudiantForm(forms.ModelForm):
    class Meta:
        model = ChargerProjetEtudiant
        fields = ['projet','fichier_traite']
        
    projet = forms.ModelChoiceField(
        queryset=Projet.objects.filter(statut='en cours'),
        label='Sélectionnez le projet à soumettre',
        empty_label='Sélectionnez un projet',
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )