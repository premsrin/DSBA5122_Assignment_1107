import streamlit as st
import plotly.express as px
import pandas as pd

@st.cache
def get_data(url):
    return pd.read_csv(url)
@st.cache
def get_co2_data(): 
    # OWID Data on CO2 and Greenhouse Gas Emissions
    # Creative Commons BY license
    CO2DATA = pd.read_csv('CO2DATA.csv')
    return CO2DATA


st.set_page_config(layout = "wide")

df_co2= get_co2_data()

st.markdown("""
# World CO2 emissions
The graphs below show the CO2 emissions per capita for the entire 
world and individual countries over time.
__Hover over any of the charts to see more detail__
---
""")

col2, space2, col3 = st.columns((10,1,10))

select_year = st.sidebar.selectbox("Select year to display data from:", sorted(pd.unique(df_co2['year']), reverse=1))


with col2:
    fig = px.choropleth(df_co2[df_co2['year']==select_year], locations="iso_code",
                        color="co2_per_capita",
                        hover_name="country",
                        range_color=(0,25),
                        color_continuous_scale=px.colors.sequential.Reds)
    st.plotly_chart(fig, use_container_width=True)

