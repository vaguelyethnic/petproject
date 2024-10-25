from django.db import models
from .users import User

class Pet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField(max_length=100)
    age = models.CharField(max_length = 5)
    breed = models.ForeignKey('Breed', on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)
    temperament = models.ForeignKey('Temperament', on_delete=models.SET_NULL, null=True)