# Import the Libraries

import streamlit as st
import pickle
import pandas as pd

# Nice Concrete Photo

from PIL import Image
im = Image.open("taylor-smith-PJMKu7RQNJ8-unsplash.jpg")
st.image(im, width = 700, caption = "by Taylor Smith, unsplash.com")

# App Title

html_temp = """
<div style="background-color:blue;padding:1.5px">
<h1 style="color:white;text-align:center;">Compresssive Strength Prediction </h1>
</div><br>"""
st.markdown(html_temp,unsafe_allow_html=True)

# Get the Input Values From Sidebar 

st.sidebar.title('Please Enter the Following Parameters')

cement=st.sidebar.slider("Amount of Cement", 102, 540, step=5)
slag=st.sidebar.slider("Amount of Slag", 0,360, step=5)
flyash=st.sidebar.slider("Amount of Flyash", 0,200, step=1)
water=st.sidebar.slider("Amount of Water", 120, 250, step=1)
superplasticizer=st.sidebar.slider("Amount of Superplasticizer", 0, 32, step=1)
coarseaggregate=st.sidebar.slider("Amount of Coarseaggregate", 800, 1145, step=1)
fineaggregate=st.sidebar.slider("Amount of Fineaggregate", 594, 993, step=1)
age=st.sidebar.slider("Age in Days", 1, 365, step=1)

# Prepare a Python Dictionary Using the Input Values 

def csMPa():
    my_dict = {"cement" :cement,
        "slag":slag,
        "flyash": flyash,
        "water": water ,
        "superplasticizer": superplasticizer,
        "coarseaggregate": coarseaggregate,
        "fineaggregate": fineaggregate,
        "age":age}
    
    df_sample = pd.DataFrame.from_dict([my_dict])
    return df_sample


dfc = csMPa()

model = pickle.load(open("model_xg", "rb"))

if st.sidebar.button("Submit"):
    result = (model.predict(dfc))
    st.success(f"Compressive Strength Prediction of the Concrete is {result} MPa")  
