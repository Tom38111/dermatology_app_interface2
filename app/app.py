import streamlit as st
from PIL import Image

import numpy as np
import pandas as pd

st.markdown("""# Dermatology app
## The application that help you to know if something is wrong on your skin
Given a skin image, it will predict if it is  malignant or benign using a model of IA""")


image = Image.open('app/raw_data/dermatologie2.jpg')
st.image(image, caption='Melanoma check-up', use_container_width=True)

with st.form(key='params_for_api'):

    st.file_uploader('Please paste a skin image')

    st.radio('Please select a model of IA', ['Convolutional Neural Network (CNN)','Pre-trained model'])

    st.markdown('''Please note that a dermatology app is not a diagnostic tool and cannot replace or substitute a visit to your doctor''')

    st.form_submit_button('Make prediction')
