from django.db import models

# Create your models here.
TAMANIO_OPCIONES = (
    ("1", "Individual"),
    ("2", "Grande"),
    ("3", "Familiar"),
)
class Pizzas(models.Model):
    
    nombre = models.CharField(max_length=30)
    foto = models.CharField(max_length=9999999)
    tamanio = models.CharField(
        max_length=20,
        choices=TAMANIO_OPCIONES,
          )
    ingredientes = models.CharField(max_length=60)
    precio = models.IntegerField() 