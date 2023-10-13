from rest_framework import serializers
from pokemons.models import Pokemon
from pokemons import const


class PokemonLightSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ("name", "hp", "attack", "defence")


class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = (
            "name",
            "type_1",
            "type_2",
            "total",
            "hp",
            "attack",
            "defence",
            "sp_attack",
            "sp_defence",
            "speed",
            "generation",
            "legendary",
        )


class ImportPokemonSerializer(serializers.Serializer):
    name = serializers.CharField()
    type_2 = serializers.CharField(allow_null=True)
    total = serializers.IntegerField()
    hp = serializers.IntegerField()
    attack = serializers.IntegerField()
    defence = serializers.IntegerField()
    sp_attack = serializers.IntegerField()
    sp_defence = serializers.IntegerField()
    speed = serializers.IntegerField()
    generation = serializers.IntegerField()
    legendary = serializers.BooleanField()
