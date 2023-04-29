########## GUI Imports
import streamlit as st
from streamlit_folium import st_folium
import folium

from ressources import StyleHelpers
from ressources import Macros
from shapely.geometry import shape

StyleHelpers.add_dlr_logo_to_page()

########## Data Processing ##########

import geopandas as gpd
import os  

# Map Title
st.title("Spatial Visualization")
st.info("In this page, the user is able to get insights into the predicted and actual prices of different neighborhood across German cities.")
st.write("---")

def execute_iteraction(city_name):

    if city_name == "Berlin":
        hbf_coordinate = Macros.BERLIN_HBF
        map= gpd.read_file(Macros.PATH_BERLIN_DATA)
    elif city_name == "Bremen":
        hbf_coordinate = Macros.BREMEN_HBF
        map= gpd.read_file(Macros.PATH_BREMEN_DATA)
    elif city_name == "Dresden":
        hbf_coordinate = Macros.DRESDEN_HBF
        map= gpd.read_file(Macros.PATH_DRESDEN_DATA)
    elif city_name == "Koln":
        hbf_coordinate = Macros.KOELN_HBF
        map= gpd.read_file(Macros.PATH_KOLN_DATA)
    else:
        hbf_coordinate = Macros.FRANKFURT_HBF
        map= gpd.read_file(Macros.PATH_FRANKFURT_DATA)

    POI_coord =  gpd.GeoSeries([hbf_coordinate], crs='EPSG:4326')

    m = map.explore(height=500, width=1000, name="Neighborhoods")
    district_centroid = map.geometry.centroid.to_crs(epsg=3035)
    district_centroid.distance(POI_coord.to_crs(epsg=3035).iloc[0])

    ########## Variables ##########
    # first latitude then longitude 
    last_neighborhoods_coords = [0, 0]
    last_neighborhoods_fid = 0
    last_click_coords = [0, 0]

    # Create a FeatureGroup for the markers
    marker_group = folium.FeatureGroup(name='Markers')

    # Add a marker to the FeatureGroup
    marker = folium.Marker([hbf_coordinate.y, hbf_coordinate.x])
    marker.add_to(marker_group)
    marker_group.add_to(m)

    # Create a LayerControl widget for the map
    layer_ctrl = folium.LayerControl()
    m.add_child(layer_ctrl)

    POI_marker = folium.LayerControl().add_to(m)

    # call to render Folium map in Streamlit
    st_data = st_folium(m, width=725)

    if st_data['last_active_drawing'] is not None:

        ########## Get FID and Coords ##########
        last_neighborhoods_fid = st_data['last_active_drawing']['properties']['Neighborhood_FID']
        last_click_coords = [st_data['last_clicked']['lat'], st_data['last_clicked']['lng']]

        ########## Get centroid from Area ##########
        polygon_coords = st_data['last_active_drawing']['geometry']
        coord = shape(polygon_coords).centroid
        last_neighborhoods_coords = [coord.y, coord.x] #longitude / latitude

        #layer_ctrl.remove_layer(marker_group)

        # st.metric("last neighborhoods FID:",last_neighborhoods_fid )
        # st.metric("last neighborhoods center coords: {}{}".format, last_neighborhoods_coords)
        # st.metric("last click coords:", last_click_coords)
        # return last_neighborhoods_fid, last_neighborhoods_coords, last_click_coords

col1, col2, col3 = st.columns(3)
col1.markdown("## Input")
city = col1.selectbox("Which city would you like to predict the prices", Macros.GERMAN_CITIES)
if (city != None):
    execute_iteraction(city)
    col2.markdown("## Output")
    col2.metric("Model Estimated Price", 1000, 300)
    col3.metric("Actual Neighboorhood Price:", 500, 250)
    # col2.metric("Last neighborhoods FID:", district_fid)
else:
    col1.warning("Please choose a city to analyze.")

