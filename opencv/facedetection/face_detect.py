import streamlit as st
import numpy as np
from PIL import Image
import cv2 as opcv
import resize

st.title("Face Detection using HaarCascaade: Simple App")
st.header("You can upload a picture or Take one using your Camera")
st.write("Please upload a picture below:")
pic = st.file_uploader("Upload a pic")

st.divider()

picture = st.camera_input("Take a picture")

if pic is not None:
    # loading
    with st.spinner("Loading"):
        # converting streamlit img to pil img
        pil_img = Image.open(pic)
        # converting the pil img to numpy array
        img = np.array(pil_img)
        # procedding with image as array
        haar_cascade = opcv.CascadeClassifier('haar_face.xml')

        faces_rect = haar_cascade.detectMultiScale(
            img, scaleFactor=1.1, minNeighbors=3)

        for (x, y, w, h) in faces_rect:
            opcv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    st.image(img, channels="RGB")
    st.warning(
        "This algorithm is NOT very smart and will get confused in many pictures. Will upload BETTER algorithms.")

elif picture:
    # loading
    with st.spinner("Loading"):
        # converting streamlit img to pil img
        pil_img = Image.open(picture)
        # converting the pil img to numpy array
        img = np.array(pil_img)
        # procedding with image as array
        haar_cascade = opcv.CascadeClassifier('haar_face.xml')

        faces_rect = haar_cascade.detectMultiScale(
            img, scaleFactor=1.1, minNeighbors=3)

        for (x, y, w, h) in faces_rect:
            opcv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

    st.image(img, channels="RGB")
    st.warning(
        "This algorithm is NOT very smart and will get confused in many pictures. Will upload BETTER algorithms.")
# print(f'Number of faces found is: {len(faces_rect)}')


# opcv.imshow('Detected faces', img)
