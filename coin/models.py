from django.db import models

# Create your models here.
class Space(models.Model):
    title = models.CharField(max_length=200)
    create_date = models.DateField(auto_now_add=True)
    content = models.TextField()