import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Mando", page_icon="🧠")

st.title('Novus Mando ⚙️')
st.header("Monitor 📺 + Alarmas ⚠️ + Recomendaciones 🧠")
st.subheader("Aluche, Madrid - YoComproEn_MetroSt24 📝")
st.markdown('ACTIVA EL MONITOR: Carga tu archivo')

#DATA
cargararchivo = st.file_uploader('Carga el archivo de ventas depurado de YoComproEn')
if cargararchivo:
    st.header("Monitor de YoComproEn_MetroSt24 📝 ")
    col1, col2, col3 = st.columns(3)
    col1.metric(label ="Ventas Agregadadas", value = '7.572€', delta='27Jun4Nov')
    col2.metric("Ventas Máquina A", "86,18%", "27Jun4Nov")
    col3.metric("Ventas Máquina B", "13,81%", "27Jun4Nov")
    df = pd.read_csv(cargararchivo)
 
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Sales quantity'], y=df['Sales amount'])
    ax.set_xlabel('Hora')
    ax.set_ylabel('VentasTotalesXHora')
    st.pyplot(fig)
    
    st.write(df.describe())
    st.dataframe(df)
    
    st.header('Alarmas de Aluche, Madrid - YoComproEn_MetroSt24 📝')
    alarma1, alarma2, alarma3 = st.columns(3)
    alarma1.metric("Productos - vendidos", "1/2/18", "-85%prom")
    alarma2.metric("Horarios - vendidos", "16h.13h.18h", "-73%prom")
    alarma3.metric("Inventario + rotación", "8-32-33", "485%prom")
    st.write(df.head())

    st.header('Recomendaciones de Aluche, Madrid - YoComproEn_MetroSt24 📝')
    recomendacion1, recomendacion2, recomendacion3 = st.columns(3)
    recomendacion1.metric("Productos + vendidos", "1/2/18", "85%prom")
    recomendacion2.metric("Horarios + vendidos", "16h.13h.18h", "73%prom")
    recomendacion3.metric("Inventario - rotación", "8-32-33", "-485%prom")
    st.write(df.head())

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
