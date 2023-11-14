import streamlit as st
from api_process import fetch_api_data
import requests


title,url,content = fetch_api_data()


# retrieve image from url and store locally to render
image_data = requests.get(url)
image_path = "img.jpg"
with open(image_path,'wb') as file:
    file.write(image_data.content)

st.set_page_config(layout='wide')
st.title(title)
st.image(image_path)
st.write(content)