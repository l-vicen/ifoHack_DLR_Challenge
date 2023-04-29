import streamlit as st
from ressources import HelperFunctions

import folium
import geopandas as gpd
from streamlit_folium import st_folium

HelperFunctions.add_dlr_logo_to_page()

# Map Title
st.title("Map")

#neighborhoods_berlin= gpd.read_file("test.gpkg")
neighborhoods_berlin= gpd.read_file("./data/1 Land Prices/Land_Prices_Neighborhood_Berlin.gpkg")
f = folium.Figure(width=2000, height=500)

m = neighborhoods_berlin.explore(height=500, width=1000, name="Neighborhoods").add_to(f)
folium.LayerControl().add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=1000)