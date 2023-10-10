from django.contrib import admin
from pokemons.models import Pokemon, PokemonType


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass


@admin.register(PokemonType)
class PokemonTypeAdmin(admin.ModelAdmin):
    pass
