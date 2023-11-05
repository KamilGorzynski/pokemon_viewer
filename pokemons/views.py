import pandas as pd
from django.db import connection
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from pokemons.utils import get_extension
from pokemons.const import EXTENSIONS, FILE_COLUMNS
from pokemons.tasks import create_pokemons_task
from pokemons.models import Pokemon, PokemonType
from pokemons.plotly import get_strongest_pokemons_chart_div


class SamplePokemonsList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    # ? is translated 'ORDER BY RANDOM()' in SQL
    queryset = Pokemon.objects.order_by("?")

    def list(self, request):
        sample_amount = int(request.query_params.get("amount", 3))
        df = pd.read_sql_query(
            str(self.get_queryset()[:sample_amount].query), connection
        )
        return Response(
            df.replace({"nan": None})
            .replace(
                {"type_1_id": {obj.id: obj.name for obj in PokemonType.objects.all()}}
            )
            .rename(columns={"type_1_id": "type_1"})
            .sort_values(by="name")
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


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
@cache_page(60 * 3)
def strongest_pokemons(request):
    df = pd.read_sql_query(str(Pokemon.objects.all().query), connection).replace(
        {"type_1_id": {obj.id: obj.name for obj in PokemonType.objects.all()}}
    )

    max_attack_indices = df.groupby("type_1_id")["attack"].idxmax()
    result = df.loc[max_attack_indices, ["type_1_id", "name", "attack"]].reset_index(
        drop=True
    )

    return render(
        request,
        "plotly_main.html",
        context={"plot_div": get_strongest_pokemons_chart_div(result)},
    )
