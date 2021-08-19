from rest_framework import serializers
from .models import Cancion


class CancionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cancion
        fields = ('nombre', 'fecha', 'duracion', 'album', 'artista', 
        'banda', 'genero', 'subgenero', 'similares', 'labels', 'instrumentos')