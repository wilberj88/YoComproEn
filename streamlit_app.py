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
st.header("Análisis de Datos de YoComproEn_MetroSt24")
st.write("Ventas, Precios y Ubicaciones")

#DATA
precios = pd.DataFrame('PreciosProductosAlucheDepurados27jun4nov.xlsx')
st.line_chart(precios)
