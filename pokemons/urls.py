from django.urls import path
from pokemons.viewsets import LightPokemonViewSet
from pokemons.views import import_pokemons


urlpatterns = [
    path('list/', LightPokemonViewSet.as_view({'get': 'list'})),
    path('import/', import_pokemons, name="import"),
]