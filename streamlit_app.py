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
st.write("Información de ventas y precios entre el 27 de junio y el 4 de noviembre de 2022")

st.markdown('##Principales resultados')

col1, col2, col3 = st.columns(3)
col1.metric(label ="Ventas", value = '7.572€')
col2.metric("Productos para 50% Ventas", "3", "-1")
col3.metric("Productos Inferiores al 1% ventas", "86%", "4%")

#DATA
precios = pd.read_excel('/PreciosProductosAlucheDepurados27jun4nov.xlsx')
st.dataframe(precios)
