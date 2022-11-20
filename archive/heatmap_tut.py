import pandas as pd
from folium import Map
from folium.plugins import HeatMap

df = pd.read_csv('data.txt')
df = df.drop(columns=['Unnamed:'])

for_map = Map(location=[30.169621, -96.683617], zoom_start=8, )