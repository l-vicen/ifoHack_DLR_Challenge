import streamlit as st
from ressources import Macros 

# Sidebar Style Configuration Helper Method
def add_dlr_logo_to_page():

    # DLR Logo 
    add_logo()

    # Contributors
    st.sidebar.markdown('##### Contributors')
    st.sidebar.markdown('Billy Herrmann')
    st.sidebar.markdown('Justin Zhang')
    st.sidebar.markdown('Lucas Perasolo')
    st.sidebar.markdown('Rohan Walia')
    st.sidebar.markdown('Sandro Barrius')

# Sidebar Logo with CSS Styling
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://www.dlr.de/static/media/Logo-en.bc10c5b6.svg);
                background-repeat: no-repeat;
                padding-top: 135px;
                background-position: 60px 75px;
            }
            [data-testid="stSidebarNav"]::before {
                margin-left: 100px;
                margin-top: 30px;
                margin-bottom: 100px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )