import altair as alt
import pandas as pd

def grafico_categoria(df):
    if df.empty:
        return None
    df_group = df.groupby("Categoria")["Importo"].sum().reset_index()
    chart = alt.Chart(df_group).mark_arc().encode(
        theta="Importo",
        color="Categoria",
        tooltip=["Categoria", "Importo"]
    )
    return chart
