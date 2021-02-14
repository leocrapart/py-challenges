import streamlit as st
import pages.poete 
import pages.ideas

st.set_page_config(page_icon="random", layout="wide")

PAGES = {
    "Le poète": pages.poete,
    "Idees": pages.ideas
}


with st.sidebar:
    "# Challenges"
    selection =  st.radio("", list(PAGES.keys()))
    page = PAGES[selection]

page.app()




    
