import datetime
import base64
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.linear_model import LinearRegression

st.set_page_config(
    page_title="Bike Sharing Prediction",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.markdown(
    """
    <style>
        .css-hby737, .css-17eq0hr, .css-qbe2hs {
            background-color:    #154360    !important;
            color: black !important;
        }
        div[role="radiogroup"] {
            color:black !important;
            margin-left:8%;
        }
        div[data-baseweb="select"] > div {
            
            color: black;
        }
        div[data-baseweb="base-input"] > div {
            background-color: #aab7b8 !important;
            color: black;
        }
        
        .st-cb, .st-bq, .st-aj, .st-c0{
            color: black !important;
        }
        .st-bs, .st-ez, .st-eq, .st-ep, .st-bd, .st-e2, .st-ea, .st-g9, .st-g8, .st-dh, .st-c0 {
            color: black !important;
        }
        .st-fg, .st-fi {
            background-color: #c6703b !important;
            color: black !important;
        }
        
        .st-g0 {
            border-bottom-color: #c6703b !important;
        }
        .st-fz {
            border-top-color: #c6703b !important;
        }
        .st-fy {
            border-right-color: #c6703b !important;
        }
        .st-fx {
            border-left-color: #c6703b !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.markdown('<h1 style="margin-left:8%; color:#FA8072">Bike Sharing Prediction</h1>', unsafe_allow_html=True)

add_selectbox = st.sidebar.radio(
    "",
    ("About", "Bike Sharing Prediction", "Conclusion")
)
def pima():
    pickle_in = open('SVM_model.pkl', 'rb')
    classifier = pickle.load(pickle_in)

    st.markdown("## Pima Indian Diabetes Disease prediction.")
    
    st.markdown('#### Diabetes Prediction(Only for females above 21years of Age)')
    name = st.text_input("Name:")
    pregnancy = st.number_input("No. of times pregnant:", min_value=0, max_value=15, step=1)
    glucose = st.number_input("Plasma Glucose Concentration :", min_value=40, max_value=250, step=1)
    bp =  st.number_input("Diastolic blood pressure (mm Hg):", min_value=20, max_value=140, step=1)
    skin = st.number_input("Triceps skin fold thickness (mm):", min_value=5, max_value=80, step=1)
    insulin = st.number_input("2-Hour serum insulin (mu U/ml):", min_value=0, max_value=1000, step=1)
    bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):", min_value=10, max_value=100, step=1)
    dpf = st.number_input("Diabetes Pedigree Function:", min_value=0.0, max_value=2.5, step=1.0)
    age = st.number_input("Age:", min_value=10, max_value=120, step=1)
    submit = st.button('Predict')

    if submit:
            prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
            if prediction == 0:
                st.write('Congratulation',name,'You are not diabetic')
            else:
                st.write(name," we are really sorry to say but it seems like you are Diabetic.")
if add_selectbox == 'About':
    
    st.subheader('ABOUT THE PROJECT')

    st.markdown('<h4>Project Goals</h4>', unsafe_allow_html=True)
    st.markdown('', unsafe_allow_html=True) 
    	
	
elif add_selectbox == 'Bike Sharing Prediction':
	
    st.subheader('BIKE SHARING PREDICTION')


elif add_selectbox == 'Conclusion':
    
    st.subheader('CONCLUSION')
    
    st.markdown('', unsafe_allow_html=True)
