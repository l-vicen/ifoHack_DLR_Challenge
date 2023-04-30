import streamlit as st
from ressources import StyleHelpers
from PIL import Image

# Sidebar Configuration
StyleHelpers.add_dlr_logo_to_page()

# Title
st.title("Home")

# Information
st.info("Welcome to the Tarantula's Team submission. In our app, you are able to get insight into land prices across German cities. Our prediction is based on a simple feature we have created called: SpiderNetz.")
st.markdown("---")

st.markdown("## The Tarantula's Centroid Spider-Web Algorithm")
st.markdown("###### Even if Tarantula's do not produce spider webs")

st.info("Our methodology comes down to calculating the distance between the central point of neighborhoods (so called \"Centroid\") to specific points of interest (e.g. Hauptbahnhof (HBF)). Our feature engineering process is based on our algorithm, which for every feature returns a vector containing the distances of every Centroid to a POI.")

image = Image.open("assets/algo.png")
st.image(image)

st.markdown("###### Steps of the algorithm")
st.markdown("1. Determination of centroids. The determination of centroids involves identifying the geographic center point of a given city district")
st.markdown("2. Distance to main train station. The Euclidean distance is a measure of the straight-line distance between two points in a two- or three-dimensional space. In this case, we used it to calculate the distance between each district's centroid and the main train station in Berlin.")
st.markdown("3. FID/ Feature analysis. The analysis of the features and involved a combination of geographic analysis and statistical modeling to understand the spatial relationships that are driving land prices")
st.write("---")

st.markdown("## Our Features")
imageTwo = Image.open("assets/diagram_approach.png")
st.image(imageTwo)

