import app1
import app2
import streamlit as st
PAGES = {
    "Part Number": app1,
    "Part Family": app2
}
st.sidebar.title('Aequs/Geater/GS Bid Analysis')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()