from django.db import models

# ckeditor
from ckeditor.fields import RichTextField

# Create your models here.

class Organoleptica(models.Model):
    fecha = models.DateField()
    punto_muestreo = models.CharField(max_length=50)
    presenta_color = models.BooleanField(choices=((True, 'Si'), (False, 'No')))
    presenta_olor = models.BooleanField(choices=((True, 'Si'), (False, 'No')))
    presenta_sabor = models.BooleanField(choices=((True, 'Si'), (False, 'No')))
    particulas_extrañas = models.BooleanField(choices=((True, 'Si'), (False, 'No')))
    responsable = models.CharField(max_length=50)
    observaciones = RichTextField()

    def __str__(self) -> str:
        return self.punto_muestreo + ' ' + str(self.fecha)