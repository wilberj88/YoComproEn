import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Solutions", page_icon="🧠")

st.title('Novus Solutions')
st.header("Análisis de Datos 🔍 de YoComproEn_MetroSt24 📝 ")
st.markdown('Principales resultados')

col1, col2, col3 = st.columns(3)
col1.metric(label ="Ventas Agregadadas", value = '7.572€', delta='27Jun4Nov')
col2.metric("Ventas Máquina A", "86,18%", "27Jun4Nov")
col3.metric("Ventas Máquina B", "13,81%", "27Jun4Nov")

#DATA
cargararchivo = st.file_uploader('Carga el archivo de ventas depurado')
df = pd.read_csv(cargararchivo)
st.dataframe(df)

st.write("Desagregación de Ventas por Ubicación")
#datos
df = pd.DataFrame(
np.random.randn(1000, 2) / [50, 50] + [40.25, 3.42],
columns=['lat', 'lon'])
st.pydeck_chart(pdk.Deck(
map_style=None,
initial_view_state=pdk.ViewState(
    latitude=40.25,
    longitude=3.42,
    zoom=11,
    pitch=50,
),
layers=[
    pdk.Layer(
       'HexagonLayer',
       data=df,
       get_position='[lon, lat]',
       radius=200,
       elevation_scale=4,
       elevation_range=[0, 1000],
       pickable=True,
       extruded=True,
    ),
    pdk.Layer(
        'ScatterplotLayer',
        data=df,
        get_position='[lon, lat]',
        get_color='[200, 30, 0, 160]',
        get_radius=200,
    ),
    ],
    ))
