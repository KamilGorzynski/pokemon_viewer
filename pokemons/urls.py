from django.urls import path
from pokemons.viewsets import LightPokemonViewSet


urlpatterns = [
    path('list/', LightPokemonViewSet.as_view({'get': 'list'})),
]