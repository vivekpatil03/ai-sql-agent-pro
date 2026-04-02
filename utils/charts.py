import plotly.express as px

def create_chart(df):

    if len(df.columns) < 2:
        return None

    fig = px.bar(
        df,
        x=df.columns[0],
        y=df.columns[1],
        title="Data Visualization",
        template="plotly_dark"
    )

    return fig