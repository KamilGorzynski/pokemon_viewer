from rest_framework import viewsets
from pokemons.models import Pokemon
from pokemons.serializers import PokemonLightSerializer


class LightPokemonViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonLightSerializer