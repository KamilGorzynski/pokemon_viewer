import pandas as pd
import plotly.colors as colors
from plotly.offline import plot
from plotly.graph_objs import Bar, Figure
from django.db import connection
from django.shortcuts import render
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
        df = (
            pd.read_sql_query(str(self.get_queryset().query), connection)
            .replace({"type_1_id": {obj.id: obj.name for obj in PokemonType.objects.all()}})
        )
        max_attack_indices = df.groupby("type_1_id")["attack"].idxmax()
        result = df.loc[max_attack_indices, ["type_1_id", "name", "attack"]].reset_index(drop=True)

        fig = Figure(layout={
            "title": 'Strongest pokemons by type',
            "xaxis_title": 'Type',
            "yaxis_title": 'Attack value',
        })
        fig.add_trace(Bar(
            x=result["type_1_id"].to_list(),
            y=result["attack"].to_list(),
            marker_color=colors.DEFAULT_PLOTLY_COLORS,
            text=result["name"].to_list()
        ))
        plot_div = plot(fig, output_type='div')
        return render(request, "plotly_main.html", context={'plot_div': plot_div})


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
