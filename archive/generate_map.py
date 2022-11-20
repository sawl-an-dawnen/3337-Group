import plotly.graph_objects as go
from server_plot import server_plot

def plotly_heatmap(window, w_depth, w_mag):
    df1 = window
    
    elevation = (df1.iloc[:, 4]*w_depth) + (df1.iloc[:, 3]*w_mag)
    df1.insert(5, column="elevation", value=elevation)
    
    fig = go.Figure(go.Densitymapbox(lat=df1.latitude, lon=df1.longitude, z=df1.elevation, radius=15))
    fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
    fig.update_layout(margin={"r":0, "t":0, "l":0, "b":0})
    
    server_plot(fig)

