import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from unittest import mock


@pytest.fixture
def csv_file():
    file_content = b"""
        #,Name,Type 1,Type 2,Total,HP,Attack,Defense,Sp. Atk,Sp. Def,Speed,Generation,Legendary
        1,Bulbasaur,Grass,Poison,318,45,49,49,65,65,45,1,False
        2,Ivysaur,Grass,Poison,405,60,62,63,80,80,60,1,False
    """
    return SimpleUploadedFile('pokemon.csv', file_content)


@pytest.fixture
def txt_file():
    file_content = b''
    return SimpleUploadedFile('pokemon.txt', file_content)


@pytest.fixture
def no_extension_file():
    file_content = b''
    return SimpleUploadedFile('pokemon', file_content)


@pytest.mark.django_db
def test_file_not_provided(client):
    response = client.post("/pokemons/import/", {}, format='multipart')
    assert response.json() == {"error": "File not provided"}


@pytest.mark.django_db
def test_incorrect_extension(client, txt_file):
    response = client.post("/pokemons/import/", {'file': txt_file}, format='multipart')
    assert response.json() == {'error': 'Incorrect extension'}


@pytest.mark.django_db
def test_no_extension(client, no_extension_file):
    response = client.post("/pokemons/import/", {'file': no_extension_file}, format='multipart')
    assert response.json() == {"error": "File has no extension"}


@pytest.mark.django_db
@mock.patch("pokemons.views.create_pokemons_task.delay")
def test_import(task_mock, client, csv_file):
    response = client.post("/pokemons/import/", {'file': csv_file}, format='multipart')
    assert response.status_code == 200
    assert response.json() == {"message": "Loading objects in progress"}
    task_mock.assert_called_once()
