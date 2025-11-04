import altair as alt

def grafico_categoria(df_user):
    if df_user.empty:
        return None
    chart = alt.Chart(df_user).mark_bar().encode(
        x='Categoria',
        y='Importo',
        color='Tipo',
        tooltip=['Categoria', 'Importo', 'Tipo']
    )
    return chart
