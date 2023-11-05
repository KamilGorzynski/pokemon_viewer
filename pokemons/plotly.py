import plotly.colors as colors
from plotly.offline import plot
from plotly.graph_objs import Bar, Figure
from pandas import DataFrame


def get_strongest_pokemons_chart_div(result: DataFrame) -> plot:
    fig = Figure(
        layout={
            "title": "Strongest pokemons by type",
            "xaxis_title": "Type",
            "yaxis_title": "Attack value",
        }
    )
    fig.add_trace(
        Bar(
            x=result["type_1_id"].to_list(),
            y=result["attack"].to_list(),
            marker_color=colors.DEFAULT_PLOTLY_COLORS,
            text=result["name"].to_list(),
        )
    )
    return plot(fig, output_type="div")
