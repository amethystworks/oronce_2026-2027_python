from rest_framework import serializers 
from .models import Pokemon

class PokemonSerializer (serializers.ModelSerializer):
    class Meta:
        name = serializers.CharField(max_length=50)
        
        
        
   