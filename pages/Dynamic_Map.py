########## GUI Imports
import streamlit as st
from streamlit_folium import st_folium
import folium
from ressources import StyleHelpers
from ressources import Macros
from ressources.model_predictor import model as impModel

########## Data Processing ##########
import geopandas as gpd
from shapely.geometry import shape

# Sidebar Style
StyleHelpers.add_dlr_logo_to_page()

# Map Title
st.title("Spatial Visualization")
st.info("In this page, the user is able to get insights into the predicted and actual prices of different neighborhood across German cities.")
st.write("---")

dataframe_total, pca, rf = impModel.preprocessing()

st.markdown("## Input")
city = st.selectbox("Which city would you like to predict the prices", Macros.GERMAN_CITIES)

if "markers" not in st.session_state:
   st.session_state["markers"] = []

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
    elif city_name == "Köln":
        hbf_coordinate = Macros.KOELN_HBF
        map= gpd.read_file(Macros.PATH_KOLN_DATA)
    else:
        hbf_coordinate = Macros.FRANKFURT_HBF
        map= gpd.read_file(Macros.PATH_FRANKFURT_DATA)

    m = map.explore(height=500, width=1000, name="Neighborhoods")

    ########## Variables ##########
    # first latitude then longitude 
    last_neighborhoods_coords = [0, 0]
    last_neighborhoods_fid = 0
    last_click_coords = [0, 0]

    # Marker updating magic
    fg = folium.FeatureGroup(name="Markers")
    for marker in st.session_state["markers"]:
        fg.add_child(marker)
    if "last_clicked" not in st.session_state:
       st.session_state["last_clicked"] = None

    # call to render Folium map in Streamlit
    st_data = st_folium(m, feature_group_to_add=fg, height=450, width=1000,)

    if st_data['last_active_drawing'] is not None:
        ########## Get FID and Coords ##########
        last_neighborhoods_fid = st_data['last_active_drawing']['properties']['Neighborhood_FID']
        last_click_coords = [st_data['last_clicked']['lat'], st_data['last_clicked']['lng']]

        ########## Get centroid from Area ##########
        polygon_coords = st_data['last_active_drawing']['geometry']
        coord = shape(polygon_coords).centroid
        last_neighborhoods_coords = [coord.y, coord.x] # longitude / latitude

        random_marker = folium.Marker(location=last_neighborhoods_coords , icon=folium.Icon(color='red'),)
        hbf_marker = folium.Marker(location=[hbf_coordinate.y, hbf_coordinate.x], icon=folium.Icon(color='red'),)
        line = folium.PolyLine([last_neighborhoods_coords , (hbf_coordinate.y, hbf_coordinate.x)], color="red", weight=2, opacity=1).add_to(m)
        st.session_state["markers"].clear()
        st.session_state["markers"].append(random_marker)
        st.session_state["markers"].append(hbf_marker)
        st.session_state["markers"].append(line)
        
        if ( st_data["last_clicked"] and st_data["last_clicked"] != st.session_state["last_clicked"]):
            st.session_state["last_clicked"] = st_data["last_clicked"]
            st.experimental_rerun()
        
        return last_neighborhoods_fid
    
fdi = execute_iteraction(city)

st.markdown("---")
st.markdown("## Output")
if (fdi != None):
    actual_price, model_price = impModel.predictor(fdi, city, dataframe_total, pca, rf)
    col1, col2, col3 = st.columns(3)
    col1.metric("Actual Price ($)", round(actual_price, 2))
    col2.metric("Predicted Price ($)", round(float(model_price), 2))
    ratio = round(float(model_price / actual_price  * 100),2)
    col3.metric("Precision Ratio (%)", ratio)

    if ((float(actual_price) == -1) and (float(model_price) == -1)):
        st.warning("No values exist because this neighborhood had compromised data and has been disconsidered.")
    else:
        if (ratio >= 70 and ratio <= 130):
            st.success("Reasonable Prediction")
        elif (ratio >= 130):
            st.error("Overestimation")
        else:
            st.error("Underestimation")
else:
    st.warning("Click on a city neighborhood and discover what it has to offer!")