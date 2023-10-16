from rest_framework import viewsets
from pokemons.models import Pokemon
from pokemons.serializers import PokemonLightSerializer


class LightPokemonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pokemon.objects.only("name", "hp", "attack", "defence")
    serializer_class = PokemonLightSerializer
