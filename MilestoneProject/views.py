from django.shortcuts import render, redirect
from .forms import ProjetForm,ChargerProjetEtudiantForm
from .models import Projet,ChargerProjetEtudiant
#from .models import ProjetPrecedent
from django.contrib.auth.decorators import login_required


# Create your views here.

def charger_projet(request):
    if request.method == 'POST':
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_projets')
    else:
        form = ProjetForm()
    return render(request, 'charger_projet.html', {'form': form})

def liste_projets(request):
    projets = Projet.objects.all()
    return render(request, 'liste_projets.html', {'projets': projets})



def telecharger_projet_etudiant(request, projet_id):
    projet = Projet.objects.get(pk=projet_id)
    return render(request, 'telecharger_projet_etudiant.html', {'projet': projet})

def charger_projet_etudiant(request):
    if request.method == 'POST':
        form = ChargerProjetEtudiantForm(request.POST, request.FILES)
        if form.is_valid():
            projet = form.cleaned_data['projet']
            projet.statut = 'soumis'
            projet.fichier_projet_traite = form.cleaned_data['fichier_traite']
            projet.save()
            return redirect('liste_projets_etudiant')
    else:
        form = ChargerProjetEtudiantForm()

    return render(request, 'charger_projet_etudiant.html', {'form': form})

def liste_projets_etudiant(request):
    projets_etudiant = Projet.objects.filter(statut='soumis')
    return render(request, 'liste_projets_etudiant.html', {'projets_etudiant': projets_etudiant})

def telecharger_projet_soumis(request, projet_id):
    projet = Projet.objects.get(pk=projet_id)
    return render(request, 'telecharger_projet_soumis.html', {'projet': projet})






# def liste_projets_archives(request):
#     projets_archives = ProjetPrecedent.objects.filter(statut='archivé')
#     return render(request, 'liste_projets_archives.html', {'projets_archives': projets_archives})


# #@login_required
# def liste_projets_enseignant(request):
#     utilisateur_connecte = request.user

#     projets_enseignant = Projet.objects.filter(createur=utilisateur_connecte)

#     return render(request, 'liste_projets_enseignant.html', {'projets_enseignant': projets_enseignant})
