from django.db import models

class Temperament(models.Model):
    name = models.CharField(max_length=100, unique=True)