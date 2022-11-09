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
st.set_page_config(layout="wide", page_title="Novus Mando", page_icon="⚙️")

st.title('Novus Mando ⚙️ - YoComproEn  🛒')

option = st.selectbox(
    'Elige la tienda de análisis',
    ('Aluche, Madrid', 'Talavera', 'Toledo'))
if option == 'Aluche, Madrid':
    st.write('Tienda Aluche, Madrid. Datos del 27 de junio de 2022 a 4 de noviembre de 2022: 130 días ☀️ con sus noches 🌛')

st.write('---')
st.write("""
**Tecnología Novus Solutions**
- ⚙️: `Monitores de Ventas por Horas y Productos` con `Alarmas de Bajas Ventas` y `Recomendaciones para más Ventas`
""")
st.write('---')



#MONITOR 1: HORARIOS
st.header("Monitor 📺 de Ventas por Horarios ⏰")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Hora Top 1 en Ventas", value = '1am', delta='362%')
col2.metric("Hora Top 2 en Ventas", "0am", "317%")
col3.metric("Hora Top 3 en Ventas", "2am", "289%")


hora_seleccionada = st.slider(
    "Selecciona una hora de análisis", 0, 23)

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])

st.write("Desagregación geográfica  de las ventas para la hora ", hora_seleccionada, "en las tiendas de Madrid")

st.write(
    pdk.Deck(map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": 40.3875,
            "longitude": -3.7575416667,
            "zoom": 12,
            "pitch": 50},
        layers=[
            pdk.Layer(
                'HexagonLayer',
                data=df,
                get_position='[lon, lat]',
                radius=150,
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

st.markdown('CONCLUSIONES MONITOR HORAS:')
st.text('Las horas de mayor facturación son en la madrugada (1h,0h,2h), seguido de la mañana (8am,9am,10am)')


#MONITOR 2: PRODUCTOS
st.header("Monitor 📺 de Ventas por Productos 🛒")
col1, col2, col3 = st.columns(3)
col1.metric(label ="Ventas Agregadadas", value = '7.572€', delta='27Jun4Nov')
col2.metric("Ventas Máquina A", "86,18%", "27Jun4Nov")
col3.metric("Ventas Máquina B", "13,81%", "27Jun4Nov")


x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Ventas Julio', 'Ventas Agosto', 'Ventas Septiembre']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .25, .5])
# Plot!
st.plotly_chart(fig, use_container_width=True)

st.write('Top 3 de mejores productos y horas')
st.write(pd.DataFrame({
    'ID Productos más vendidos': [8, 32, 33],
    'Horas de mayores ventas': [1, 0, 2]}))



st.markdown('CONCLUSIONES MONITOR PRODUCTOS:')
st.text('3 productos (ID=8,32,33) de 38 generan más del 50% de la facturación de los últimos 130 días')


#ALARMAS
st.header("Alarmas de Bajas Ventas ⚠️")

alarma1, alarma2, alarma3 = st.columns(3)
alarma1.metric("Productos - vendidos", "1/2/18", "-85%prom")
alarma2.metric("Horarios - vendidos", "16h.13h.18h", "-73%prom")
alarma3.metric("Inventario + rotación", "8-32-33", "485%prom")

chart_data = pd.DataFrame(np.random.randn(23, 3), columns=["Efectivo", "TarjetaCrédito", "TarjetaDébito"])
st.area_chart(chart_data)
    
st.write('ID TOP 1 Producto de menor facturación', 1)
st.write('ID TOP 2 Producto de menor facturación', 2)
st.write('ID TOP 3 Producto de menor facturación', 18)

st.markdown('CONCLUSIONES ALARMAS ⚠️:')
st.text('3 productos (ID=1,2,18) están concentrando la peor facturación de los últimos 130 días')
st.text('Las horas de menor facturación son en la tarde (16h,13h,18h)')



#RECOMENDACIONES
st.header("Recomendaciones para Aumentar Ventas 🧠")

rec1, rec2, rec3 = st.columns(3)
rec1.metric("Horario de mayor potencial de crecimiento", "4pm", "85%prom")
rec2.metric("Productos de mayor potencial de crecimiento", "ID_08", "73%prom")
rec3.metric("Productos sin tracción requerida para matenerse", "1-2-18", "-45%prom")

st.text('Potenciales zonas de mayor facturación')

df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [40.3875, -3.7575416667],
    columns=['lat', 'lon'])

st.map(df)

st.markdown('CONCLUSIONES RECOMENDACIONES 🧠:')
st.text('Se puede crecer 117% la facturación si se equlibran las ventas en los horarios de 4pm y 1pm')
st.text('Se puede aumentar la rentabilidad en 35% si se aumentan las ventas de los productos con ID_007 y ID_004')

st.caption('Todos los análisis son representativos únicamente entre el 27 de junio de 2022 a 4 de noviembre de 2022: 130 días ☀️ con sus noches 🌛')

