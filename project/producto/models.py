from django.db import models

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    tamaño = models.CharField(max_length=50)
    distribuidor = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nombre} {self.tamaño}"

class Snack(models.Model):
    tipo = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    gramaje = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.tipo} {self.marca} {self.gramaje}"

class Chocolate(models.Model):
    marca = models.CharField(max_length=50)
    gramaje = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80)

    def __str__(self) -> str:
        return f"{self.marca} {self.descripcion} {self.gramaje}"
