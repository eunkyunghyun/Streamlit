from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
import requests
import streamlit as st
import pandas as pd
import numpy as np

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(city):
    city = city.replace(" ", "+")
    res = requests.get('https://www.google.com/search?q={}&oq={}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8'.format(city, city), headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    st.write(location, time, info, weather + '°C')
    app = Nominatim(user_agent='tutorial')
    location = app.geocode(location)
    df = pd.DataFrame(np.random.randn(1, 1) / [50, 50] + [list(location)[1][0], list(location)[1][1]], columns=['lat', 'lon'])
    st.map(df)


name = st.selectbox('City', ('Seoul', 'Busan', 'Incheon', 'Daegu', 'Gwangju', 'Daejeon', 'Ulsan', 'Jeju'))
name = name + " weather"
weather(name)
