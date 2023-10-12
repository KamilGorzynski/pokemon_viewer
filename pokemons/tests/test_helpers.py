import pytest
import pandas as pd

from django.core.files.uploadedfile import SimpleUploadedFile
from pokemons.models import PokemonType, Pokemon
from pokemons.helpers import create_pokemons_types, create_pokemons


@pytest.fixture
def csv_file():
    file_content = b"""
        #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
        1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False
        2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False
    """
    return SimpleUploadedFile('pokemon.csv', file_content)


@pytest.mark.django_db
def test_create_pokemon_types(csv_file):
    pokemon_types_dict = create_pokemons_types(pd.read_csv(csv_file))
    pokemon_type_queryset = PokemonType.objects.all()
    pokemon_type_name = "Grass"

    assert pokemon_type_queryset.count() == 1
    assert pokemon_type_queryset.values_list("name", flat=True).first() == pokemon_type_name
    assert pokemon_types_dict == {pokemon_type_name: pokemon_type_queryset.first()}


@pytest.mark.django_db
def test_create_pokemons(csv_file):
    create_pokemons(pd.read_csv(csv_file))
    assert Pokemon.objects.count() == 2
