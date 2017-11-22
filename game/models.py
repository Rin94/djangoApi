from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

# Create your models here.

def value_validator(value):

    if value <= 0 or value >=10000:
        raise ValidationError(
            _('%(value)s is not on accepted range numbers'), params={'value': value}

        )


class Desarrolladora (models.Model):
    id= models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=150)

    def __str__(self):
        return self.nombre


class Juego (models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    fecha_publicacion= models.DateField(blank=True, null=True)
    precio= models.PositiveIntegerField(default=999, validators=[value_validator])
    desarrolladora=models.ForeignKey(Desarrolladora)
