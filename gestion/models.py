
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class Utilisateur(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('client', 'Client'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Client(models.Model):
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    entreprise = models.CharField(max_length=100)

class Ressource(models.Model):
    TYPE_CHOICES = [('salle', 'Salle'), ('bureau', 'Bureau'), ('materiel', 'Matériel')]
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    capacité = models.IntegerField()
    description = models.TextField()
    dispo = models.BooleanField(default=True)

class Réservation(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    ressource = models.ForeignKey(Ressource, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    statut = models.CharField(max_length=20, default='en attente')

class Paiement(models.Model):
    reservation = models.OneToOneField(Réservation, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=8, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, default='en attente')

User = get_user_model()
class Equipement(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Espace(models.Model):
    nom = models.CharField(max_length=100)
    capacité = models.PositiveIntegerField()
    équipements = models.ManyToManyField(Equipement, blank=True)
    description = models.TextField()
    disponibilité = models.BooleanField(default=True)

    def __str__(self):
        return self.nom

class Reservation(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    espace = models.ForeignKey(Espace, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    statut = models.CharField(
        max_length=20,
        choices=[('en_attente', 'En attente'), ('confirmée', 'Confirmée'), ('annulée', 'Annulée')],
        default='en_attente'
    )

    def __str__(self):
        return f"{self.espace.nom} par {self.utilisateur.username}"