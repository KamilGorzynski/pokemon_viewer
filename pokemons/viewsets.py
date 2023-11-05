from rest_framework import viewsets
from rest_framework import permissions
from pokemons.models import Pokemon
from pokemons.serializers import PokemonLightSerializer


class LightPokemonViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Pokemon.objects.only("name", "hp", "attack", "defence")
    serializer_class = PokemonLightSerializer
