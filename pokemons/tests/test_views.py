import pytest
from unittest import mock
from pokemons.tests.factories import PokemonFactory, PokemonTypeFactory


@pytest.mark.django_db
def test_sample(client):
    type_1 = PokemonTypeFactory()
    PokemonFactory(type_1=type_1)
    PokemonFactory(type_1=type_1)
    PokemonFactory(type_1=type_1)

    response = client.get("/pokemons/sample/", {})
    assert response.status_code == 200
    assert response.json() == [
        {
            "id": mock.ANY,
            "name": "pokemon-name-0",
            "type_1": "pokemon-type-name-0",
            "type_2": "type_2",
            "total": 15,
            "hp": 20,
            "attack": 20,
            "defence": 20,
            "sp_attack": 20,
            "sp_defence": 20,
            "speed": 20,
            "generation": 1,
            "legendary": False,
        },
        {
            "id": mock.ANY,
            "name": "pokemon-name-1",
            "type_1": "pokemon-type-name-0",
            "type_2": "type_2",
            "total": 15,
            "hp": 20,
            "attack": 20,
            "defence": 20,
            "sp_attack": 20,
            "sp_defence": 20,
            "speed": 20,
            "generation": 1,
            "legendary": False,
        },
        {
            "id": mock.ANY,
            "name": "pokemon-name-2",
            "type_1": "pokemon-type-name-0",
            "type_2": "type_2",
            "total": 15,
            "hp": 20,
            "attack": 20,
            "defence": 20,
            "sp_attack": 20,
            "sp_defence": 20,
            "speed": 20,
            "generation": 1,
            "legendary": False,
        },
    ]


@pytest.mark.django_db
def test_sample_no_pokemons(client):
    response = client.get("/pokemons/sample/", {})
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_wrong_method(client):
    response = client.post("/pokemons/sample/", {})
    assert response.status_code == 405
