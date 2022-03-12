from bs4 import BeautifulSoup
import requests
import streamlit as st
import numpy as np
import pandas as pd

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
response = requests.get(url)
movies = []
items = []
directions = []
data = []
rows = []

if response.status_code == 200:
    source = response.text
    soup = BeautifulSoup(source, 'html.parser')
    top_list = soup.findAll("div", {"class": "tit3"})
    fluctuation = soup.findAll("td", {"class": "range ac"})
    for i in range(2, 52):
        direction = soup.select("#old_content > table > tbody > tr:nth-child({}) > td:nth-child(3)".format(i))
        try:
            direction = str(direction[0]).split(' ')[2].split('=')[1].split('"')[1]
            directions.append(direction)
        except IndexError:
            directions.append("na")
    for i in range(0, len(fluctuation)):
        item = int(fluctuation[i].text)
        if directions[i] == "up":
            items.append(item)
        elif directions[i] == "down":
            items.append(-item)
        else:
            items.append(0)
    for i in range(len(top_list)):
        data.append(top_list[i].text.strip())
        rows.append(i + 1)
        movies.append("{}: {}".format(i + 1, top_list[i].text.strip()))
else:
    print(response.status_code)

st.title("Movie Ranking")
col1, col2 = st.columns(2)

with col1:
    st.header("Ranking")
    df = pd.DataFrame(data, index=rows, columns=["Movie"])
    st.write(df)
with col2:
    st.header("Fluctuation")
    arr = np.array(items)
    chart_data = pd.DataFrame(arr, index=np.arange(1, 51,), columns=["Fluctuation"])
    st.bar_chart(chart_data)
