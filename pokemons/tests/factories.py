import factory
from pokemons.models import Pokemon, PokemonType


class PokemonTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PokemonType

    name = factory.Sequence(lambda n: f"pokemon-type-name-{n}")


class PokemonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pokemon

    name = factory.Sequence(lambda n: f"pokemon-name-{n}")
    type_1 = factory.SubFactory(PokemonTypeFactory)
    type_2 = "type_2"
    total = 15
    hp = 20
    attack = 20
    defence = 20
    sp_attack = 20
    sp_defence = 20
    speed = 20
    generation = 1
    legendary = False
