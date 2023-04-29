import streamlit as st
import folium

def display_Network(vector_neighborhoods, list_centroids):
    m = folium.Map(location=[40.720, -73.993],
                zoom_start=15)

    loc = [(40.720, -73.993),
        (40.721, -73.996)]

    folium.PolyLine(loc,
                    color='red',
                    weight=15,
                    opacity=0.8).add_to(m)
    m

