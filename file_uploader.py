from PIL import Image
import streamlit as st
import global_file
from ocr import ocr
from categorise import categorise as ctg
def file_uploader():
    img_data = st.file_uploader(label='Load image for recognition', type=['png', 'jpg'], 
                                accept_multiple_files=True, key='file_uploader_1')

    if img_data:
        uploaded_img = Image.open(img_data[0])

        if len(img_data) > 1:
            comparision_img = Image.open(img_data[1])
            global_file.Comparision_Image = comparision_img
        else:
            comparision_img = None

        global_file.Uploaded_Image = uploaded_img
        return uploaded_img, comparision_img
    else:
        return None, None

def show_image():
    if global_file.Uploaded_Image is not None:
        st.image(global_file.Uploaded_Image)

        ocr(global_file.Uploaded_Image)
        ctg(global_file.Url)
    else:
        st.warning("No image uploaded yet.")

    st.divider()

    if global_file.Comparision_Image is not None:
        st.image(global_file.Comparision_Image)
        ocr(global_file.Comparision_Image)
        st.subheader(global_file.Url)
        ctg(global_file.Url)
    else:
        st.warning("No image uploaded yet.")