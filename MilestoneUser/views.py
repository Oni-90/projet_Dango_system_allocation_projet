from django.shortcuts import render, redirect
from .forms import InscriptionForm, ConnexionForm
from django.contrib.auth import login, logout


# Create your views here.

# Vues pour l'inscription et la connexion
def inscription(request):
    if request.method == 'GET':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('connexion')  
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = ConnexionForm(request.POST)
        if form.is_valid():
            # Authentifie l'utilisateur
            user = form.post_user()
            login(request, user)
            
          
            return redirect('liste_projets')
    else:
        # Affiche le formulaire de connexion vide en cas de méthode GET
        form = ConnexionForm()
    
    return render(request, 'connexion.html', {'form': form})





