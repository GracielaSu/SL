import streamlit as st
from PIL import Image
img=Image.open("images.png")
st.image(img, width=200) #display image

if st.checkbox("Show/Hide"):
    st.text("Showing the widget")
    st.image(img,width=50)

status= st.radio("Select Colour: ", ("Blue","Green","Yellow"))
st.success(status)