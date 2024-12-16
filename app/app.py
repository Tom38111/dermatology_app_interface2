import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd

image1 = Image.open('raw_data/dermatology_app.png')
st.image(image1, width=300)

st.markdown('<span style="font-size: 24px;">The application that help you to know if something is wrong on your skin</span>', unsafe_allow_html=True)

st.markdown("""## The application that help you to know if something is wrong on your skin
Given a skin image, it will predict if it is malignant or benign using a model of IA""")


image = Image.open('raw_data/dermatologie2.jpg')
st.image(image, caption='Melanoma check-up', use_container_width=True)

with st.form(key='params_for_api'):

    uploaded_file = st.file_uploader('Please paste a skin image')

    st.radio('Please select a model of IA', ['Convolutional Neural Network (CNN)','Pre-trained model'])

    st.markdown('''Please note that a dermatology app is not a diagnostic tool and cannot replace or substitute a visit to your doctor''')

    st.form_submit_button('Make prediction')


if uploaded_file is not None:

    params = uploaded_file

    dermatology_app_api_url = 'https://dermatology_app_api.lewagon.ai/predict'
    response = requests.get(dermatology_app_api_url, params=params)

    prediction = response.json()

    pred = prediction['???']

    st.header(f'Fare amount: ${round(pred, 2)}')
