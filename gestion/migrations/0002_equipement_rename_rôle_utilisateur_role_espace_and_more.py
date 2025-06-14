# Generated by Django 5.2.1 on 2025-06-05 14:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='utilisateur',
            old_name='rôle',
            new_name='role',
        ),
        migrations.CreateModel(
            name='Espace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('capacité', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('disponibilité', models.BooleanField(default=True)),
                ('équipements', models.ManyToManyField(blank=True, to='gestion.equipement')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('statut', models.CharField(choices=[('en_attente', 'En attente'), ('confirmée', 'Confirmée'), ('annulée', 'Annulée')], default='en_attente', max_length=20)),
                ('espace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.espace')),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
