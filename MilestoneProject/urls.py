from django.urls import path
from . import views

urlpatterns = [
    path('charger_projet/', views.charger_projet, name='charger_projet'),

    path('liste_projets/', views.liste_projets, name='liste_projets'),
    
    path('telecharger_projet_etudiant/<int:projet_id>/', views.telecharger_projet_etudiant, name='telecharger_projet_etudiant'),
    
    path('charger_projet_etudiant/', views.charger_projet_etudiant, name='charger_projet_etudiant'),

    path('liste_projets_etudiant/', views.liste_projets_etudiant, name='liste_projets_etudiant'),

    path('telecharger_projet_soumis/<int:projet_id>/', views.telecharger_projet_soumis, name='telecharger_projet_soumis'),

]
