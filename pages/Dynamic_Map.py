########## GUI Imports
import streamlit as st
from streamlit_folium import st_folium
import folium
from ressources import StyleHelpers
from ressources import Macros
from ressources.model_predictor import model

########## Data Processing ##########
import geopandas as gpd
from shapely.geometry import shape

# Sidebar Style
StyleHelpers.add_dlr_logo_to_page()

# Map Title
st.title("Spatial Visualization")
st.info("In this page, the user is able to get insights into the predicted and actual prices of different neighborhood across German cities.")
st.write("---")

st.markdown("## Input")
city = st.selectbox("Which city would you like to predict the prices", Macros.GERMAN_CITIES)

def execute_iteraction(city_name):

    if city_name == "Berlin":
        map= gpd.read_file(Macros.PATH_BERLIN_DATA)
    elif city_name == "Bremen":
        map= gpd.read_file(Macros.PATH_BREMEN_DATA)
    elif city_name == "Dresden":
        map= gpd.read_file(Macros.PATH_DRESDEN_DATA)
    elif city_name == "Koln":
        map= gpd.read_file(Macros.PATH_KOLN_DATA)
    else:
        map= gpd.read_file(Macros.PATH_FRANKFURT_DATA)

    m = map.explore(height=500, width=1000, name="Neighborhoods")

    ########## Variables ##########
    # first latitude then longitude 
    last_neighborhoods_coords = [0, 0]
    last_neighborhoods_fid = 0
    last_click_coords = [0, 0]

    # Create a FeatureGroup for the markers
    marker_group = folium.FeatureGroup(name='Markers')

    # Add a marker to the FeatureGroup
    marker_group.add_to(m)

    # Create a LayerControl widget for the map
    layer_ctrl = folium.LayerControl()
    m.add_child(layer_ctrl)

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

        st.write("last neighborhoods FID: {}".format(last_neighborhoods_fid))
        return last_neighborhoods_fid
    
fdi = execute_iteraction(city)

st.markdown("---")
st.markdown("## Output")
if (fdi != None):
    actual_price, model_price = model.apply_predictor(fdi)
    st.metric("Actual Price", actual_price, 300)
    st.metric("Model Suggested Price", model_price, 250)
    st.success("Prediction Terminated.")
else:
    st.warning("Click on a city neighborhood and discover what it has to offer!")