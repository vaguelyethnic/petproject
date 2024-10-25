from django.db import models
from .users import User
from .pets import Pet

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'pet') 