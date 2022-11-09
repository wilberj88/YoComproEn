import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import altair as alt
import pydeck as pdk
import matplotlib.pyplot as plt
import datetime


# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Mando", page_icon="🧠")

st.title('Novus Mando ⚙️ - YoComproEn  🛒')
st.text('Monitor + Alarmas + Recomendaciones')
option = st.selectbox(
    'Elige la tienda de análisis',
    ('Aluche, Madrid', 'Talavera', 'Toledo'))
if option == 'Aluche, Madrid':
    st.write('You selected:', option)
    st.caption('Tienda Aluche, Madrid. Datos del 27 de junio de 2022 a 4 de noviembre de 2022: 130 días ☀️ con sus noches 🌛')




#MONITOR
st.header("Monitor de Horarios y Productos 📺")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Ventas Agregadadas", value = '7.572€', delta='27Jun4Nov')
col2.metric("Ventas Máquina A", "86,18%", "27Jun4Nov")
col3.metric("Ventas Máquina B", "13,81%", "27Jun4Nov")
st.write(1234)

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])

st.write(c)

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))
st.text('This is some text.')

#ALARMAS
st.header("Alarmas de Bajas Ventas ⚠️")
st.write('1 + 1 = ', 2)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
st.text('This is some text.')

#RECOMENDACIONES
st.header("Recomendaciones para Aumentar Ventas 🧠")
st.write(1234)
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
}))
st.text('This is some text.')

st.caption('Datos del 27 de junio de 2022 a 4 de noviembre de 2022: 130 días ☀️ con sus noches 🌛')




#DATA
cargararchivo = st.file_uploader('Carga el archivo de ventas depurado de YoComproEn')
if cargararchivo:
    st.header("Monitor de YoComproEn_MetroSt24 📝 ")
    col1, col2, col3 = st.columns(3)
    col1.metric(label ="Ventas Agregadadas", value = '7.572€', delta='27Jun4Nov')
    col2.metric("Ventas Máquina A", "86,18%", "27Jun4Nov")
    col3.metric("Ventas Máquina B", "13,81%", "27Jun4Nov")
    df = pd.read_csv(cargararchivo)
 
    st.line_chart(df)
    
    st.bar_chart(df)
    
    st.area_chart(df)
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Sales amount'], y=df['TrSalePrice'])
    ax.set_xlabel('Sales amount')
    ax.set_ylabel('TrSalePrice')
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
    recomendacion1.metric("Productos + vendidos", "8-32-33", "85%prom")
    recomendacion2.metric("Horarios + vendidos", "1h.0h.2h", "73%prom")
    recomendacion3.metric("Inventario - rotación", "1-2-18", "-485%prom")
    st.write(df.head())

    st.write("Georeferenciación de las Ventas")
    #datos
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
    st.map(df)
    
    df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [43.47, 3.41],
    columns=['lat', 'lon'])
    st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=43.47,
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
