from dataclasses import dataclass
from django.db import models

# Create your models here.

class Space(models.Model):
    title = models.CharField(max_length=200)
    data = models.DateField()
    content = models.TextField()