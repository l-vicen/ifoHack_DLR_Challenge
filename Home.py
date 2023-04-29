import streamlit as st
from ressources import StyleHelpers

# Page Config
st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

# Sidebar Configuration
StyleHelpers.add_dlr_logo_to_page()

# Title
st.title("Home")