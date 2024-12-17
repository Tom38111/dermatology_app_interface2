import streamlit as st
from PIL import Image
import os
import numpy as np
import pandas as pd
import requests
import io

image1 = Image.open('raw_data/dermatology_app.png')
st.image(image1, width=400)

st.markdown('<span style="font-size: 23px;">The application that help you to know if something is wrong on your skin</span>', unsafe_allow_html=True)

st.markdown("""Given a skin image, it will predict if it is malignant or benign using a model of IA""")

image = Image.open('raw_data/dermatologie2.jpg')
st.image(image, caption='Melanoma check-up', use_container_width=True)

image2 = Image.open('raw_data/melanoma_13.jpg')
image3 = Image.open('raw_data/melanoma_11.jpg')
image4 = Image.open('raw_data/melanoma_0.jpg')

with st.form(key='params_for_api'):

    uploaded_file = st.file_uploader('1 - Please paste a skin image')

    st.markdown('<span style="font-size: 13px;">If you do not have a skin picture, drag and drop one of these images</span>', unsafe_allow_html=True)
    st.image((image2, image3, image4), width=100)

    model_type = st.radio('2 - Please select a model of IA', ['Convolutional Neural Network (CNN) 1','Convolutional Neural Network (CNN) 2','Pre-trained model'])

    st.markdown('''Please note that dermatology app is not a diagnostic tool and cannot substitute a visit to your doctor''')


    submitted = st.form_submit_button('Make prediction')


if submitted is not None and uploaded_file is not None:

    st.image(uploaded_file, width=200)
    st.write("Filename: ", uploaded_file.name)

    uploaded_file = uploaded_file.read()

    files = {'image': io.BytesIO(uploaded_file)}

    if model_type == 'Convolutional Neural Network (CNN) 1':

        st.write('Convolutional Neural Network (CNN) 1')

        response = requests.post('https://dermatologyapp-325653398443.europe-west1.run.app/predict_cnn', files=files)

        prediction = response.json()

        st.markdown(f'<span style="font-size: 24px;">:blue[{prediction['answer']}]</span>', unsafe_allow_html=True)

    if model_type == 'Convolutional Neural Network (CNN) 2':

        st.write('Convolutional Neural Network (CNN) 2')

        response = requests.post('https://dermatologyapp-325653398443.europe-west1.run.app/predict_cnn_bis', files=files)

        prediction = response.json()

        st.markdown(f'<span style="font-size: 24px;">:blue[{prediction['answer']}]</span>', unsafe_allow_html=True)

    if model_type == 'Pre-trained model':

        st.write('Pre-trained model')

        response = requests.post('https://dermatologyapp-325653398443.europe-west1.run.app/predict_ptm', files=files)

        prediction = response.json()

        st.markdown(f'<span style="font-size: 24px;">:blue[{prediction['answer']}]</span>', unsafe_allow_html=True)
