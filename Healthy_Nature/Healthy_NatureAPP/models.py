from django.db import models

# Create your models here.
class Personnels(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    salaire = models.FloatField(max_length=10)
    tel = models.CharField(max_length=20)
    adresse = models.CharField(max_length=100)