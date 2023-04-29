import streamlit as st
from ressources import StyleHelpers

# Sidebar Configuration
StyleHelpers.add_dlr_logo_to_page()

# Title
st.title("Home")

# Information
st.info("Welcome to the Tarantulas Submission. In our app, you are able to get insight into land prices across German cities. Our prediction is based on a simple feature we have created called: SpiderNetz.")