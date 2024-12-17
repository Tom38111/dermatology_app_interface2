import streamlit as st
from PIL import Image
import os
import numpy as np
import pandas as pd
import requests

image1 = Image.open('raw_data/dermatology_app.png')
st.image(image1, width=400)

st.markdown('<span style="font-size: 23px;">The application that help you to know if something is wrong on your skin</span>', unsafe_allow_html=True)

st.markdown("""Given a skin image, it will predict if it is malignant or benign using a model of IA""")


image = Image.open('raw_data/dermatologie2.jpg')
st.image(image, caption='Melanoma check-up', use_container_width=True)

with st.form(key='params_for_api'):

    uploaded_file = st.file_uploader('Please paste a skin image')

    model_type = st.radio('Please select a model of IA', ['Convolutional Neural Network (CNN) 1','Convolutional Neural Network (CNN) 2','Pre-trained model'])

    st.markdown('''Please note that dermatology app is not a diagnostic tool and cannot substitute a visit to your doctor''')


    submitted = st.form_submit_button('Make prediction')


if submitted is not None and uploaded_file is not None:

    params = uploaded_file
    os.write(1, f"{model_type}\n".encode())

    dermatology_app_api_url_1 = 'https://dermatologyapp-325653398443.europe-west1.run.app/docs/predict_cnn'
    dermatology_app_api_url_2 = 'https://dermatologyapp-325653398443.europe-west1.run.app/docs/predict_cnn_bis'
    dermatology_app_api_url_3 = 'https://dermatologyapp-325653398443.europe-west1.run.app/docs/predict_ptm'

    if model_type == 'Convolutional Neural Network (CNN) 1':

        response = requests.get('https://dermatologyapp-325653398443.europe-west1.run.app/docs/predict_cnn', params=params)

        prediction = response.json()

        st.header(prediction)

    if model_type == 'Convolutional Neural Network (CNN) 2':

        response = requests.get('https://dermatologyapp-325653398443.europe-west1.run.app/docs/predict_cnn_bis', params=params)

        prediction = response.json()

        st.header(prediction)

    if model_type == 'Pre-trained model':

        response = requests.get('https://dermatologyapp-325653398443.europe-west1.run.app/docs/predict_ptm', params=params)

        prediction = response.json()

        st.header(prediction)
