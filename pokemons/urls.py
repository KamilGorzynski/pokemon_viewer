from django.urls import path
from pokemons.viewsets import LightPokemonViewSet
from pokemons.views import import_pokemons, StrongestPokemonsList, SamplePokemonsList


urlpatterns = [
    path("light_list/", LightPokemonViewSet.as_view({"get": "list"})),
    path("strongest/", StrongestPokemonsList.as_view(), name="strongest"),
    path("sample/", SamplePokemonsList.as_view(), name="sample"),
    path("import/", import_pokemons, name="import"),
]
