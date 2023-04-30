import streamlit as st
from ressources import StyleHelpers
from PIL import Image

# Sidebar Configuration
StyleHelpers.add_dlr_logo_to_page()

# Title
st.title("Home Page")

# Information
st.info("Welcome to the Tarantula's Team submission. In our app, you are able to get insight into land prices across German cities. Our prediction is based on a simple feature we have created called: SpiderNetz.")
st.markdown("---")

st.markdown("## The Tarantula's Centroid Spider-Web Algorithm")
st.markdown("###### Even if Tarantula's do not produce spider webs :joy:")

image = Image.open("assets/algo.png")
st.image(image)

st.markdown("###### Steps of the algorithm")
st.markdown("1. Determination of the central point of neighborhoods (centroids). The determination of centroids involves identifying the geographic center point of a given city district")
st.markdown("2. Distance to Points of Interest (POIs), e.g. Hauptbahnhof. The Euclidean distance is a measure of the straight-line distance between two points in a two- or three-dimensional space. In this case, we used it to calculate the distance between each district's centroid and the main train station in Berlin.")
st.markdown("3. FID / Feature analysis. The analysis of the features and involved a combination of geographic analysis and statistical modeling to understand the spatial relationships that are driving land prices")
st.write("---")

st.markdown("## Tarantula's Approach")
st.info("In our approach, we investigate the relationship between socioeconomic attributes and spatial distance measurements of different POIs and their effect on the land value.")
imageThree = Image.open("assets/diagram_approach.png")
st.image(imageThree)
st.write("---")

# st.markdown("## Tarantula's Stack")
# col1, col2, col3, col4 = st.columns(4)

# i1 = Image.open("assets/python.png")
# i2 = Image.open("assets/sklearn.png")
# i3 = Image.open("assets/streamlit.png")
# i4 = Image.open("assets/geopandas.png")

# col1.image(i1)
# col2.image(i2)
# col3.image(i3)
# col4.image(i4)

