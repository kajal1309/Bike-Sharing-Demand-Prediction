import datetime
import base64
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from sklearn.ensemble import RandomForestRegressor

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

#def pima():
if add_selectbox == 'About':
    
    st.subheader('ABOUT THE PROJECT')

    st.markdown('<h4>Project Goals</h4>', unsafe_allow_html=True)
    st.markdown('', unsafe_allow_html=True) 
    	
elif add_selectbox == 'Bike Sharing Prediction':
	
      st.subheader('BIKE SHARING PREDICTION')
      pickle_in = open('day_model_best', 'rb')
      regressor = pickle.load(pickle_in)

      st.markdown("## Bike sharing demand prediction ")
    
      st.markdown('#### On daily basis')
      name = st.text_input("Name:")
      year = st.number_input("Enter the year code : 0:2011 ,1:2012", min_value=0, max_value=1, step=1)
      month = st.number_input("Enter the month ", min_value=1, max_value=12, step=1)
      holiday          =  st.number_input("Enter code for holiday : 0:No holiday ,1:Holiday", min_value=0, max_value=1, step=1)
      workingday      = st.number_input("Enter the code for working day: 0:Non-working day , 1:working day", min_value=0, max_value=1, step=1)
      temperature     = st.number_input("Enter the normalized value of temperature:0 to 1 inclusive and step size 0.00001", min_value=0, max_value=1, step=0.00001)
      humidity         = st.number_input("Enter the normalized humidity :0 to 1 and step size 0.00001", min_value=0, max_value=1, step=0.00001)
      windspeed        = st.number_input("Enter the normalised windspeed :0 to 1 and step size 0.00001", min_value=0, max_value=1, step=0.00001)
      day             = st.number_input("Enter day of the month:1 to 31", min_value=1, max_value=31, step=1)
      weathersit_2    = st.number_input("Enter code for weathersit_2", min_value=0, max_value=1, step=1)
      weathersit_3 = st.number_input("Enter code for weathersit_3", min_value=0, max_value=1, step=1)
      weekday_Monday = st.number_input("Enter code for weekday_Monday", min_value=0, max_value=1, step=1)
      weekday_Saturday = st.number_input("Enter code for weekday_Saturday", min_value=0, max_value=1, step=1)
      weekday_Sunday = st.number_input("Enter code for weekday_Sunday", min_value=0, max_value=1, step=1)
      weekday_Thursday = st.number_input("Enter code for weekday_Thursday", min_value=0, max_value=1, step=1)
      weekday_Tuesday= st.number_input("Enter code for weekday_Tuesday", min_value=0, max_value=1, step=1)
      weekday_Wednesday = st.number_input("Enter code for weekday_Wednesday", min_value=0, max_value=1, step=1)
      submit = st.button('Predict')

      if submit:
            prediction = regressor.predict([[year, month, holiday,windspeed,day,weathersit_2,weathersit_3,weekday_Monday,weekday_Saturday,weekday_Sunday,weekday_Thursday,weekday_Tuesday,weekday_Wednesday]])
            st.write('Hi',name,'The predicted bike rentals is',prediction)


elif add_selectbox == 'Conclusion':
    
    st.subheader('CONCLUSION')
    
    st.markdown('', unsafe_allow_html=True)
