from django import forms
from game.models import Juego, Desarrolladora

class FormJuego(forms.ModelForm):
    nombre= forms.CharField();
    precio= forms.NumberInput();
    desarrolladora= forms.ModelChoiceField(queryset=Desarrolladora.objects.all())
    fecha_publicacion= forms.DateField()

    class Meta:
        model= Juego
        fields=(
            'nombre',
            'fecha_publicacion',
            'precio',
            'desarrolladora'
        )