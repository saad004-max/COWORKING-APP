from django.urls import path
from . import views

urlpatterns = [
    path('ressources/', views.liste_ressources, name='liste_ressources'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('espaces/', views.liste_espaces, name='liste_espaces'),
    path('espaces/<int:espace_id>/reserver/', views.reserver_espace, name='reserver_espace'),
    path('reservations/annuler/<int:reservation_id>/', views.annuler_reservation, name='annuler_reservation'),
    path('reservations/historique/', views.historique_reservations, name='historique_reservations'),
    path('calendrier/', views.vue_calendrier, name='vue_calendrier'),
    path('ressources/ajouter/', views.ajouter_ressource, name='ajouter_ressource'),

]
