import pytest
from unittest import mock
from pokemons.tests import factories as pokemon_factories
from users.tests import factories as user_factories


@pytest.mark.django_db
def test_sample(client):
    access_token = user_factories.AccessTokenFactory()
    type_1 = pokemon_factories.PokemonTypeFactory()
    pokemon_factories.PokemonFactory(type_1=type_1)
    pokemon_factories.PokemonFactory(type_1=type_1)
    pokemon_factories.PokemonFactory(type_1=type_1)

    response = client.get("/pokemons/sample/", HTTP_AUTHORIZATION=f"Bearer {access_token}")
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
    access_token = user_factories.AccessTokenFactory()
    response = client.get("/pokemons/sample/", HTTP_AUTHORIZATION=f"Bearer {access_token}")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.django_db
def test_wrong_method(client):
    access_token = user_factories.AccessTokenFactory()
    response = client.post("/pokemons/sample/", HTTP_AUTHORIZATION=f"Bearer {access_token}")
    assert response.status_code == 405

