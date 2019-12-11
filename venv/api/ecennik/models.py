from django.db import models


# Create your models here.

class Towary(models.Model):
    nazwa = models.CharField(max_length=60)
    cena = models.CharField(max_length=60)
    opis = models.CharField(max_length=60)
    miasto = models.CharField(max_length=60)
    marka = models.CharField(max_length=60)
    kategoria = models.CharField(max_length=60)



class Kupony(models.Model):
    nazwa = models.CharField(max_length=60)
    opis = models.CharField(max_length=60)
    kod = models.CharField(max_length=60)