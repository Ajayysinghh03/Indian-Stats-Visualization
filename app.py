#myyyyyyyyyyyyyyyyyyy
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config('wide')

df = pd.read_csv("IndianData.csv.csv")
list_of_states = list(df['State'].unique())
list_of_states.insert(0,"Overall India")

st.sidebar.title("INDIAN STATISTICS")
selected_state = st.sidebar.selectbox("Select a State", list_of_states)

primary = st.sidebar.selectbox("Select Primary Parameter", sorted(df.columns[6:]))
secondary = st.sidebar.selectbox("Select Secondary Parameter", sorted(df.columns[6:]))

plot = st.sidebar.button("Plot Graph")

if plot:
    st.text("Size represents Primary parameter")
    st.text("Colour represents Secondary parameter")

    if selected_state == "Overall India":
        # plot for india
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)

    else:
        # plot for state
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6, size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700,hover_name='District')

        st.plotly_chart(fig, use_container_width=True)