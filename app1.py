import streamlit as st
import pandas as pd


def app():
    st.title('Part Number')
    @st.cache
    def get_data():
        return pd.read_excel('merged_files_.xlsx')
    df = get_data()

    pn = st.text_input('Please Enter Part Number')
    df = df[df['PN'] == pn]  # Filtering the dataframe.
    st.dataframe(df)
