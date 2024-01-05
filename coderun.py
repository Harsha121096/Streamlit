# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:06:02 2023

@author: Harsha
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

loaded_model = pickle.load(open('C:/Users/Harsha/Downloads/Dissertation/ML Models/diabetes.sav','rb'))

heart_model = pickle.load(open('C:/Users/Harsha/Downloads/Dissertation/ML Models/heartdisease.sav','rb'))

def diabetesPrediction(Input):
    DBInput_array=[]
    DBInput_array = np.asarray(Input)
    DBInput_reshaped = DBInput_array.reshape(1,-1)
    DBPrediction = loaded_model.predict(DBInput_reshaped)

    if (DBPrediction[0]==1):
      return 'The person is Diabetic'
    else:
      return 'The person is not Diabetic'


def HeartDiseasePrediction(Input):
    HDInput_array =[]
    HDPrediction  =[]
    HDInput_array = np.asarray(Input)
    HDInput_reshaped = HDInput_array.reshape(1,-1)
    HDPrediction = heart_model.predict(HDInput_reshaped)

    if (HDPrediction[0]==1):
      return 'The person is at a risk of Heart Disease'
    else:
      return 'The person is not at a risk of Heart Disease'


with st.sidebar:
    selected = option_menu("Disease Prediction System", ["💉 Diabetes", '💓 Heart Disease'], 
        menu_icon="cast", default_index=0)

if (selected == '💉 Diabetes'):
    st.title('Diabetes Prediction Model')
   
    gender = st.selectbox("Select your gender:", ("Male", "Female", "Other"),index=None)
    if gender == "Male":
        gender_value = 1
    elif gender == "Female":
        gender_value = 0
    else:
        gender_value = 2
    
    age = st.number_input("Enter your age:", min_value=0, step=1)
    
    bmi = st.number_input('BMI')
    
    HbA1c_level=st.number_input('HbA1c level')
    
    blood_glucose_level=st.number_input('Blood Glucose Level')
    
    hypertension = st.selectbox("Do you have Hypertension:", ("Yes", "No"),index=None)
    if hypertension == "Yes":
        hypertension_value = 1
    else:
        hypertension_value = 0
    
    heart_disease = st.selectbox("Do you have Heart Disease:", ("Yes", "No"),index=None)
    if heart_disease == "Yes":
        heart_disease_value = 1
    else:
        heart_disease_value = 0
    
    DBresult=''
    
    if st.button('Prediction Result'):
        DBresult=diabetesPrediction([gender_value,age,hypertension_value,heart_disease_value,bmi,HbA1c_level,blood_glucose_level])
    
    st.success(DBresult)

#Heart Disease Prediction

if (selected == '💓 Heart Disease'):
    st.title('Heart Disease Prediction Model')
    
    Sex = st.selectbox("Select your gender:", ("Male", "Female"),index=None)
    if Sex == "Female":
        Sex_value = 0
    else:
        Sex_value = 1
    
    age_groups = [
    '18-24', '25-29', '30-34', '35-39', '40-44', '45-49',
    '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older']
    age_values = list(range(len(age_groups)))
    age_mapping = dict(zip(age_groups, age_values))
    selected_age_group = st.selectbox("Select Age Group", options=age_groups, index =None)
    if selected_age_group:
      age_value = age_mapping[selected_age_group]
   # else:
   #    st.warning("Please select an age group.")
    bmi = st.number_input('BMI')
    
    sleeptime = st.number_input('how many hours of sleep do you get in a 24-hour period ?')
    
    mentalhealth = st.number_input('For how many days during the past 30 days was your mental health not good?')
    
        
    DiffWalking = st.selectbox("Do you find it difficult walking?", ("Yes", "No"),index=None)
    if DiffWalking == "Yes":
        DiffWalking_value = 1
    else:
        DiffWalking_value = 0
        
    PhysicalActivity = st.selectbox("During the past month, other than your regular job, did you participate in any physical activities or exercises?", ("Yes", "No"),index=None)
    if PhysicalActivity == "Yes":
        PhysicalActivity_value = 1
    else:
        PhysicalActivity_value = 0
        
    health_groups = ['Excellent', 'Very good', 'Good', 'Fair', 'Poor']
    health_values = list(range(len(health_groups)))
    health_mapping = dict(zip(health_groups, health_values))
    selected_health_group = st.selectbox("Select your General health category", options=health_groups, index =None)
    if selected_health_group:
      health_value = health_mapping[selected_health_group]
        
    Asthma = st.selectbox("Did you ever had Asthma?", ("Yes", "No"),index=None)
    if Asthma == "Yes":
        Asthma_value = 1
    else:
        Asthma_value = 0
    
    KidneyDisease = st.selectbox("Do you have Kidney Disease?", ("Yes", "No"),index=None)
    if KidneyDisease == "Yes":
        KidneyDisease_value = 1
    else:
        KidneyDisease_value = 0
        
    Diabetic_groups = ['Yes', 'No', 'No, borderline diabetes', 'Yes (during pregnancy)']
    Diabetic_values = list(range(len(Diabetic_groups)))
    Diabetic_mapping = dict(zip(Diabetic_groups, Diabetic_values))
    selected_Diabetic_group = st.selectbox("Have you ever had Diabetes ?", options=Diabetic_groups, index =None)
    if selected_Diabetic_group:
      Diabetic_value = Diabetic_mapping[selected_Diabetic_group]
        
    Stroke = st.selectbox("Did you ever had a Stroke?", ("Yes", "No"),index=None)
    if Stroke == "Yes":
        Stroke_value = 1
    else:
        Stroke_value = 0
        
    AlcoholDrinking = st.selectbox("Do you drink Alcohol ?", ("Yes", "No"),index=None)
    if AlcoholDrinking == "Yes":
        AlcoholDrinking_value = 1
    else:
        AlcoholDrinking_value = 0

    Smoking = st.selectbox("Do you smoke ?", ("Yes", "No"),index=None)
    if Smoking == "Yes":
        Smoking_value = 1
    else:
        Smoking_value = 0
    

    HDresult=''
    
    if st.button('Prediction Result'):
        HDresult=HeartDiseasePrediction([bmi,Smoking_value,AlcoholDrinking_value,Stroke_value,mentalhealth,DiffWalking_value,Sex_value,age_value,Diabetic_value,PhysicalActivity_value,health_value,sleeptime,Asthma_value,KidneyDisease_value])
    
    st.success(HDresult)