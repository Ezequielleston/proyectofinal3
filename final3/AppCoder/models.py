from django.db import models

# Create your models here.


class Autos(models.Model):
        marca=models.CharField(max_length=50)
        modelo=models.CharField(max_length=50)
        def __str__(self):
                return f"{self.marca} - {self.modelo}"


class Motos(models.Model):
        marca=models.CharField(max_length=50)
        modelo=models.CharField(max_length=50)


class Camionetas(models.Model):
        marca=models.CharField(max_length=50)
        modelo=models.CharField(max_length=50)