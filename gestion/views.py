from .models import Ressource
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UtilisateurCreationForm, UtilisateurLoginForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Espace, Reservation
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from .models import Ressource
from .forms import RessourceForm

def liste_ressources(request):
    ressources = Ressource.objects.filter(dispo=True)
    return render(request, 'gestion/liste_ressources.html', {'ressources': ressources})


def inscription(request):
    if request.method == 'POST':
        form = UtilisateurCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('liste_ressources')
    else:
        form = UtilisateurCreationForm()
    return render(request, 'gestion/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = UtilisateurLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('liste_espaces')
    else:
        form = UtilisateurLoginForm()
    return render(request, 'gestion/connexion.html', {'form': form})

@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')

def liste_espaces(request):
    espaces = Espace.objects.all()
    return render(request, 'gestion/liste_espaces.html', {'espaces': espaces})

def liste_espaces(request):
    capacite = request.GET.get('capacite')
    espaces = Espace.objects.all()
    if capacite:
        espaces = espaces.filter(capacite__gte=capacite)
    return render(request, 'gestion/liste_espaces.html', {'espaces': espaces, 'capacite': capacite})

@login_required
def reserver_espace(request, espace_id):
    espace = get_object_or_404(Espace, pk=espace_id)
    if request.method == 'POST':
        date_debut = request.POST.get('date_debut')
        date_fin = request.POST.get('date_fin')
        #  pas de validation avancée ici
        reservation = Reservation.objects.create(
            espace=espace,
            utilisateur=request.user,
            date_debut=date_debut,
            date_fin=date_fin,
            confirme=True
        )
        print(f"Notification : Réservation créée pour {request.user} - {espace.nom} du {date_debut} au {date_fin}")
        messages.success(request, "Réservation effectuée avec succès !")
        return redirect('historique_reservations')
    return render(request, 'gestion/reserver_espace.html', {'espace': espace})

@login_required
def annuler_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id, utilisateur=request.user)
    reservation.confirme = False
    reservation.save()
    messages.info(request, "Réservation annulée.")
    print(f"Notification : Réservation annulée pour {request.user} - {reservation.espace.nom}")
    return redirect('historique_reservations')

@login_required
def historique_reservations(request):
    reservations = Reservation.objects.filter(utilisateur=request.user).order_by('-date_debut')
    return render(request, 'gestion/historique_reservations.html', {'reservations': reservations})

def vue_calendrier(request):
    reservations = Reservation.objects.filter(confirme=True)
    return render(request, 'gestion/vue_calendrier.html', {'reservations': reservations})
def is_admin(user):
    return user.is_staff or user.is_superuser

@user_passes_test(is_admin)
def ajouter_ressource(request):
    if request.method == 'POST':
        form = RessourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_ressources')
    else:
        form = RessourceForm()
    return render(request, 'ajouter_ressource.html', {'form': form})