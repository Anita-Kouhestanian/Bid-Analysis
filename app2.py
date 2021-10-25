import streamlit as st
import pandas as pd


def app():
    st.title('Part Family')
    @st.cache
    def get_data():
        return pd.read_excel('merged_files_.xlsx')
    df = get_data()
    family_part = df['Part Family_Aequs'].unique()
    family_part_choice = st.sidebar.selectbox('Select the Part Family:', family_part)
    pn = st.text_input('Please Enter Part Number')
    df = df[(df['Part Family_Aequs'] == family_part_choice) | (df['Part Family_Geater'] ==family_part_choice) | (df['Part Family_GS'] ==family_part_choice)]
    st.write(df)
    df = df[df['PN'] == pn]
    st.dataframe(df)