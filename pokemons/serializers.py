from rest_framework import serializers
from pokemons.models import Pokemon


class PokemonLightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ("name", "hp", "attack")
