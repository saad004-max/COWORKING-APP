from django.contrib import admin
from .models import Utilisateur, Client, Ressource, Réservation, Paiement , Espace

admin.site.register(Utilisateur)
admin.site.register(Client)
admin.site.register(Ressource)
admin.site.register(Réservation)
admin.site.register(Paiement)
admin.site.register(Espace)

