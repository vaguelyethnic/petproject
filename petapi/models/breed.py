from django.db import models

class Breed(models.Model):
    breed_type = models.CharField(max_length=100, unique=True)