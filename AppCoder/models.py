from django.db import models

# Create your models here.
class Pokemon(models.Model):
    nombre=models.CharField(max_length=40)
    tipo=models.CharField(max_length=30)
    numero=models.IntegerField()