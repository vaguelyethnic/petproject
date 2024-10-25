from django.db import models
from .pets import Pet
from .status import Status

class Playdate(models.Model):
    pet1 = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='playdates_as_pet1')
    pet2 = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='playdates_as_pet2')
    date = models.DateTimeField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='playdates_status')