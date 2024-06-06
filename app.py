import streamlit as st
from file_uploader import file_uploader, show_image
from model_load import Model
import time
st.set_page_config(page_title="Webpage Detection", layout="wide")
st.header("Enterface")
st.divider()

st.subheader("A website to detect the elements of a website")

uploaded_img, comparision_img = file_uploader()
time.sleep(2)

if file_uploader is not None:
    show_image()
else:
    st.warning('First upload the images')

Model.model_button()