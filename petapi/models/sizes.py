from django.db import models

class Size(models.Model):
    name = models.CharField(max_length=100, unique=True)