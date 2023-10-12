import pandas as pd

from pokemon_viewer_backend import celery_app
from pokemons.helpers import create_pokemons


@celery_app.task(bind=True)
def create_pokemons_task(self, pokemons_dict: dict) -> None:
    pokemon_df = pd.DataFrame(pokemons_dict)
    create_pokemons(pokemon_df)
