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

    district_centroid = map.geometry.centroid.to_crs(epsg=3035)
    district_centroid.distance(POI_coord.to_crs(epsg=3035).iloc[0])

    #########csv export#########
    os.makedirs('export', exist_ok=True)  
    district_centroid.distance(POI_coord.to_crs(epsg=3035).iloc[0]).shift(periods=1).to_csv('export/'+ city_name +'.csv')

execute_iteraction("Berlin")
execute_iteraction("Bremen")
execute_iteraction("Dresden")
execute_iteraction("Koln")
execute_iteraction("Frankfurt")