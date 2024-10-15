# Modèle pour les signalements
from django.db import models
class Signalement(models.Model):
    description = models.TextField()
    photo = models.ImageField(upload_to='signalements_photos/', null=True, blank=True)
    localisation_GPS = models.CharField(max_length=255)
    date_signalement = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=50, choices=[('En attente', 'En attente'), ('En cours', 'En cours'), ('Résolu', 'Résolu')], default='En attente')

    def __str__(self):
        return f'Signalement {self.id} - {self.statut}'