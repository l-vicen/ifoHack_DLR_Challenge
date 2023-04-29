import streamlit as st
from ressources import Macros 

# Sidebar Style Configuration Helper Method
def add_dlr_logo_to_page():

    # DLR Logo 
    st.sidebar.image(Macros.DLR_LOGO)

    # Contributors
    st.sidebar.markdown('---')
    st.sidebar.markdown('##### Contributors')
    st.sidebar.markdown('Billy Herrmann')
    st.sidebar.markdown('Justin Zhang')
    st.sidebar.markdown('Lucas Perasolo')
    st.sidebar.markdown('Rohan Walia')
    st.sidebar.markdown('Sandro Barrius')
    st.sidebar.markdown('---')
