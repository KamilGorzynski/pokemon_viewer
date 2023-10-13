import pandas as pd
from django.db import connection
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from pokemons.utils import get_extension
from pokemons.const import EXTENSIONS, FILE_COLUMNS
from pokemons.tasks import create_pokemons_task
from pokemons.models import Pokemon, PokemonType


class StrongestPokemonsList(generics.ListAPIView):
    queryset = Pokemon.objects.all()

    def list(self, request):
        query = str(self.get_queryset().query)
        df = pd.read_sql_query(query, connection)
        result = df.groupby("type_1_id").agg({"name": "idxmax", "attack": "max"})
        return Response(result)


class SamplePokemonsList(generics.ListAPIView):
    queryset = Pokemon.objects.all()

    def list(self, request):
        return Response(
            pd.read_sql_query(str(self.get_queryset().query), connection)
            .sample(int(request.query_params.get("amount", 3)))
            .replace({"nan": None})
            .replace({"type_1_id": {obj.id: obj.name for obj in PokemonType.objects.all()}})
            .rename(columns={"type_1_id": "type_1"})
            .to_dict(orient="records")
        )


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def import_pokemons(request):
    if not (file := request.FILES.get("file")):
        raise ValidationError({"error": "File not provided"})

    if get_extension(file.name) not in EXTENSIONS:
        raise ValidationError({"error": "Incorrect extension"})

    create_pokemons_task.delay(pd.read_csv(file, usecols=FILE_COLUMNS).to_dict())

    return Response({"message": "Loading objects in progress"})
