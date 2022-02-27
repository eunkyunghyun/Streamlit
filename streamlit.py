import streamlit as st

# Title
st.title("Title")

# Header
st.header("Header")

# SubHeader
st.subheader("SubHeader")

# Text
st.write("Hello, World!")

# Button
if st.button("Button"):
    st.write("Hello, World!")

# Check Box
if st.checkbox("Check Box"):
    st.write("Hello, World!")

# Check Box (default)
if st.checkbox("Check Box", value=True):
    st.write("Hello, World!")

# Radio Button
selected_item = st.radio("Radio Button", ("C", "Java", "Python", "C++", "C#"))
if selected_item == "C":
    st.write("C")
elif selected_item == "Java":
    st.write("Java")
elif selected_item == "Python":
    st.write("Python")

# Select Box
option = st.selectbox("Select Box", ("C", "Java", "Python", "C++", "C#"))
st.write(option)

# Multiple Box
option = st.multiselect("Multiple Box", ("C", "Java", "Python", "C++", "C#"))

# Slider
values = st.slider("Slider", 0.0, 100.0, (25.0, 75.0))
st.write("Values: ", values)

# Text Input
st.text_input("Text Input")

# Text Input (encryption)
st.text_input("Text Input", type="password")

# Number Data (default value second input args)
st.number_input("Number Data", 2)

# Multi Input Text
st.text_area("Multi Input Text", "Hello, World!")

# Date
st.date_input("date")

# Time
st.time_input("time")

# Split Column

import streamlit as st
import pandas as pd
import numpy as np

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)

with col2:
    st.header("Button")
    if st.button("Button"):
        st.write("Hello, World!")

with col3:
    st.header("Chart Data")
    chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
    st.bar_chart(chart_data)
