########## GUI Imports
import streamlit as st
from streamlit_folium import st_folium
import folium
from ressources import StyleHelpers

# Sidebar Configuration
StyleHelpers.add_dlr_logo_to_page()

########## Data Processing ##########
from shapely.geometry import shape, Point
import geopandas as gpd
import os  

# Map Title
st.title("Spatial Visualization")

def output():
    ########## Output ##########
    print("last neighborhoods FID:")
    print(last_neighborhoods_fid)
    print("last neighborhoods center coords:")
    print(last_neighborhoods_coords)
    print("last click coords:")
    print(last_click_coords)
########## Variables ##########
# first latitude then longitude 
last_neighborhoods_coords = [0, 0]
last_neighborhoods_fid = 0
last_click_coords = [0, 0]

#fixed value 
berlin_hbf = Point(13.369398652505957, 52.52508850317093)
POI_coord =  gpd.GeoSeries([berlin_hbf], crs='EPSG:4326')

########## Load GeoPackage source file ########## 
#Enable for only using testing data 
map= gpd.read_file("./data/1 Land Prices/Land_Prices_Neighborhood_Berlin.gpkg")
m = map.explore(height=500, width=1000, name="Neighborhoods")

#######################################################################################
district_centroid = map.geometry.centroid.to_crs(epsg=3035)

# Create a FeatureGroup for the markers
marker_group = folium.FeatureGroup(name='Markers')

# Add a marker to the FeatureGroup
marker = folium.Marker([berlin_hbf.y, berlin_hbf.x])
marker.add_to(marker_group)
marker_group.add_to(m)

# Create a LayerControl widget for the map
layer_ctrl = folium.LayerControl()
m.add_child(layer_ctrl)

POI_marker = folium.LayerControl().add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)

if st_data['last_active_drawing'] is not None:
    keysList = list(st_data.keys())

    ########## Get FID and Coords ##########
    last_neighborhoods_fid = st_data['last_active_drawing']['properties']['Neighborhood_FID']
    last_click_coords = [st_data['last_clicked']['lat'], st_data['last_clicked']['lng']]

    ########## Get centroid from Area ##########
    polygon_coords = st_data['last_active_drawing']['geometry']
    coord = shape(polygon_coords).centroid
    last_neighborhoods_coords = [coord.y, coord.x] #longitude / latitude
    output()






