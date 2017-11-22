from game.models import Desarrolladora, Juego
from rest_framework import serializers

class DesarrolladoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desarrolladora
        fields = ('id','nombre')




class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields =('id','nombre','fecha_publicacion','precio', 'desarrolladora')
