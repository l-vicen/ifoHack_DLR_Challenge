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

# Algorithm Description Section
st.markdown("## Tarantula's Centroid Spider-Web Algorithm")
st.markdown("###### Even if Tarantula's do not produce spider webs :joy:")
image = Image.open("assets/algo.png")
st.image(image)
st.markdown("###### Steps of the algorithm")
st.markdown("1. Determination of the central point of neighborhoods (centroids). The determination of centroids involves identifying the geographic center point of a given city district")
st.markdown("2. Calculation of the distance to Points of Interest (POIs), e.g. Hauptbahnhof. The Euclidean distance is a measure of the straight-line distance between two points in a two- or three-dimensional space.")
st.markdown("3. FID / Feature analysis. The analysis of the features and involved a combination of geographic analysis and statistical modeling to understand the spatial relationships that are driving land prices")
st.write("---")

# Porject Approach Description
st.markdown("## Tarantula's Approach")
st.markdown("###### Description")   
st.markdown("1. Data Engineering: Merging data of different shapes (land prices, buildings, Zensus, etc.) based on ")     
st.markdown("2. Generating features: Building new features by exploring other data streams such as OSM and world cover")     
st.markdown("3. Feature reduction: PCA, Covariance Examination")    
st.markdown("4. Model evaluation: Examination of different models (see Model Selection file) and scoring analysis")     
imageThree = Image.open("assets/approach.png")
st.image(imageThree)
st.write("---")

st.markdown("## Assumption-supporting Literature")
st.markdown("##### Variables that matter in Land Value")
st.write("Ma, Jun & Cheng, Jack C.P. & Jiang, Feifeng & Chen, Weiwei & Zhang, Jingcheng, 2020. Analyzing driving factors of land values in urban scale based on big data and non-linear machine learning techniques, Land Use Policy, Elsevier, vol. 94(C).")
st.markdown("##### One perspective on how cities grow")
st.write("Jianjun Wu, Rong Li, Rui Ding, Tongfei Li, Huijun Sun, City expansion model based on population diffusion and road growth, Applied Mathematical Modelling, Volume 43, 2017, Pages 1-14, ISSN 0307-904.")



