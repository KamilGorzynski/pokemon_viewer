from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=100)


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type_1 = models.ForeignKey(PokemonType, on_delete=models.SET_NULL, null=True)
    type_2 = models.CharField(max_length=30)
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defence = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defence = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    legendary = models.BooleanField()
