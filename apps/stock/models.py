from django.db import models

# Create your models here.
class Stock(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre} - precio {self.precio}'