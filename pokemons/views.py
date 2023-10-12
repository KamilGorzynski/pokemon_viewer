import pandas as pd
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from pokemons.utils import get_extension
from pokemons.const import EXTENSIONS, FILE_COLUMNS
from pokemons.tasks import create_pokemons_task


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def import_pokemons(request):
    if not (file := request.FILES.get("file")):
        raise ValidationError({"error": "File not provided"})

    if get_extension(file.name) not in EXTENSIONS:
        raise ValidationError({"error": "Incorrect extension"})

    create_pokemons_task.delay(pd.read_csv(file, usecols=FILE_COLUMNS).to_dict())

    return Response({"message": "Loading objects in progress"})
