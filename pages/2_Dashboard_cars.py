import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "cars.jpeg")
DATA_PATH = os.path.join(dir_of_interest, "data", "car.csv")

st.title("Dashboard - Car Data")

img = image.imread(IMAGE_PATH)
st.image(img)

st.header("Car Data")
df = pd.read_csv(DATA_PATH)
st.dataframe(df)


st.header("Car Data Visualization")

st.bar_chart(data = df,x = 'Car_Name' , y= "Selling_Price",use_container_width=True)


st.bar_chart(data= df, x= 'Car_Name', y="Present_Price",use_container_width=True)


st.line_chart(data= df, x= 'Selling_Price', y="Present_Price",use_container_width=True)


