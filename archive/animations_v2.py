from dash import Dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Animated GDP and population over decades'),
    #html.P("Select an animation:"),
    # dcc.RadioItems(
    #     id='animations-x-selection',
    #     options=["GDP - Scatter", "Population - Bar"],
    #     value="Population - Bar"
    # ),
    dcc.Loading(dcc.Graph(id="animations-x-graph"), type="cube")
])

@app.callback(
    Output("animations-x-graph", "figure"), 
    Input("GDP - Scatter", "value"))
def display_animated_graph(selection):
    df = px.data.gapminder() # replace with your own data source
    fig = px.scatter(
        df, x="gdpPercap", y="lifeExp", animation_frame="year", 
        animation_group="country", size="pop", color="continent", 
        hover_name="country", log_x=True, size_max=55, 
        range_x=[100,100000], range_y=[25,90])
    return fig

df = px.data.gapminder()

if __name__ == "__main__":
    app.run_server(debug=True)
    

