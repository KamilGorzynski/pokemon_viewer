import uuid

from pokemons.models import PokemonType, Pokemon
from django.db import transaction
from pokemons.serializers import ImportPokemonSerializer
from pokemons import const


def create_pokemons_types(pokemon_df):
    pokemon_types_list = []
    pokemon_types_dict = {}
    for type_name in pokemon_df[const.IMPORT_TYPE_1_COLUMN].drop_duplicates().to_list():
        pokemon_obj = PokemonType(name=type_name)
        pokemon_types_list.append(pokemon_obj)
        pokemon_types_dict[type_name] = pokemon_obj
    with transaction.atomic():
        PokemonType.objects.bulk_create(pokemon_types_list, ignore_conflicts=True)
    return pokemon_types_dict


def create_pokemons(pokemon_df):
    renamed_pokemon_df = pokemon_df.rename(columns=const.COLUMNS_NAMES_MAP)
    pokemon_types_dict = create_pokemons_types(pokemon_df)
    pokemon_list = []
    for _, pokemon in renamed_pokemon_df.iterrows():
        serializer = ImportPokemonSerializer(data=pokemon.to_dict())
        if serializer.is_valid(raise_exception=True):
            pokemon_list.append(
                Pokemon(
                    **{
                        **serializer.validated_data,
                        "type_1": pokemon_types_dict[pokemon["type_1"]],
                    }
                )
            )
    with transaction.atomic():
        Pokemon.objects.bulk_create(pokemon_list, ignore_conflicts=True)
