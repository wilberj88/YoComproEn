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
col2.metric("Ventas Máquina A", "6525,9€", "27Jun4Nov")
col3.metric("Ventas Máquina B", "1046,1€", "27Jun4Nov")

#DATA
precios = st.dataframe(pd.read_excel('/PreciosProductosAlucheDepurados27jun4nov.xlsx'))

