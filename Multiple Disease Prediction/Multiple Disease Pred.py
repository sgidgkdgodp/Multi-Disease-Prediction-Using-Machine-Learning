# -*- coding: utf-8 -*-
"""
Multiple Disease Prediction System
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# =============================================================================
# 1. LOAD SAVED MODELS
# =============================================================================

    # UPDATE THESE PATHS TO MATCH YOUR COMPUTER EXACTLY

diabetes_model = pickle.load(open('C:/Users/singh/OneDrive/Desktop/Multiple Disease Prediction/Saved Models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/singh/OneDrive/Desktop/Multiple Disease Prediction/Saved Models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/singh/OneDrive/Desktop/Multiple Disease Prediction/Saved Models/parkinsons_model.sav', 'rb'))


# =============================================================================
# 2. SIDEBAR NAVIGATION
# =============================================================================
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System using ML',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Disease Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# =============================================================================
# 3. DIABETES PREDICTION PAGE
# =============================================================================
if (selected == 'Diabetes Prediction'):

    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.number_input('Glucose Level')
        
    with col3:
        BloodPressure = st.number_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.number_input('Skin Thickness value')
        
    with col2:
        Insulin = st.number_input('Insulin Level')
        
    with col3:
        BMI = st.number_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function')
        
    with col2:
        Age = st.number_input('Age')


 #code for prediction

    diab_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        # Validation Check
        if Glucose == 0 or BloodPressure == 0 or BMI == 0 or Age == 0:
            st.warning("⚠️ Please enter valid values (not 0) for Glucose, BP, BMI, and Age.")
        else:
            input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            input_data_as_numpy_array = np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
            
            diab_prediction = diabetes_model.predict(input_data_reshaped)

            if (diab_prediction[0] == 1):
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
            
            st.success(diab_diagnosis)


# =============================================================================
# 4. HEART DISEASE PREDICTION PAGE
# =============================================================================
if (selected == 'Heart Disease Prediction'):

    st.title('Heart Disease Prediction using ML')
    
    
    
    
 #getting the input data from the user
 #columns for input fields
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Sex (1=Male, 0=Female)')
        
    with col3:
        cp = st.number_input('Chest Pain types (0-3)')
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure')
        
    with col2:
        chol = st.number_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)')
        
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results (0-2)')
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.number_input('Exercise Induced Angina (1=Yes, 0=No)')
        
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise')
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment (0-2)')
        
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy (0-3)')
        
    with col1:
        thal = st.number_input('Thal: 0=normal; 1=fixed; 2=reversable')
        
        
        

    heart_diagnosis = ''
    
    if st.button('Heart Disease Result'):
        # Validation Check
        if age == 0 or trestbps == 0 or chol == 0 or thalach == 0:
            st.warning("⚠️ Please enter valid values (not 0) for Age, BP, Cholesterol, and Heart Rate.")
        else:
            input_data = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            input_data_as_numpy_array = np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
            
            heart_prediction = heart_disease_model.predict(input_data_reshaped)

            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The person has Heart Disease. Please consult a doctor.'
            else:
                heart_diagnosis = 'The person does not have Heart Disease.'

            st.success(heart_diagnosis)


# =============================================================================
# 5. PARKINSONS PREDICTION PAGE
# =============================================================================
if (selected == 'Parkinsons Disease Prediction'):

    st.title('Parkinsons Disease Prediction using ML')

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.number_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.number_input('MDVP:Fhi(Hz)')
        
    with col3:
        flo = st.number_input('MDVP:Flo(Hz)')
        
    with col4:
        jitter_percent = st.number_input('MDVP:Jitter(%)')
        
    with col5:
        jitter_abs = st.number_input('MDVP:Jitter(Abs)')
        
    with col1:
        rap = st.number_input('MDVP:RAP')
        
    with col2:
        ppq = st.number_input('MDVP:PPQ')
        
    with col3:
        ddp = st.number_input('Jitter:DDP')
        
    with col4:
        shimmer = st.number_input('MDVP:Shimmer')
        
    with col5:
        shimmer_db = st.number_input('MDVP:Shimmer(dB)')
        
    with col1:
        apq3 = st.number_input('Shimmer:APQ3')
        
    with col2:
        apq5 = st.number_input('Shimmer:APQ5')
        
    with col3:
        apq = st.number_input('MDVP:APQ')
        
    with col4: 
        dda = st.number_input('Shimmer:DDA')
        
    with col5:
        nhr = st.number_input('NHR')
        
    with col1:
        hnr = st.number_input('HNR')
        
    with col2:
        rpde = st.number_input('RPDE')
        
    with col3:
        dfa = st.number_input('DFA')
        
    with col4:
        spread1 = st.number_input('Spread1')
        
    with col5:
        spread2 = st.number_input('Spread2')
        
    with col1:
        d2 = st.number_input('D2')
        
    with col2:
        ppe = st.number_input('PPE')

    parkinsons_diagnosis = ''
    
    if st.button('Parkinsons Disease Result'):
        # Validation Check
        if fo == 0 or fhi == 0 or flo == 0:
            st.warning("⚠️ Please enter valid Frequency values (not 0).")
        else:
            input_data = [fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
            
            input_data_as_numpy_array = np.asarray(input_data)
            input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
            
            parkinsons_prediction = parkinsons_model.predict(input_data_reshaped)

            if (parkinsons_prediction[0] == 1):
                parkinsons_diagnosis = "The person has Parkinsons Disease."
            else:
                parkinsons_diagnosis = "The person does not have Parkinsons Disease."
            
            st.success(parkinsons_diagnosis)