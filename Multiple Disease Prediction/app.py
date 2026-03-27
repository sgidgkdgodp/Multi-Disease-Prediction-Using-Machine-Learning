# -*- coding: utf-8 -*-
"""
Multiple Disease Prediction System using Machine Learning
"""

# Import required libraries
import pickle                    # used to load the saved ML models
import streamlit as st           # used to create the web app
from streamlit_option_menu import option_menu   # used to create sidebar menu


# ===================== Load Saved Models =====================
# We load our saved machine learning models using their file paths

diabetes_model = pickle.load(open('Saved Models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('Saved Models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('Saved Models/parkinsons_model.sav','rb'))


# ===================== Sidebar Menu =====================
# Sidebar allows user to select which prediction they want to perform

with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System using ML',
        ['Diabetes Prediction',
         'Heart Disease Prediction',
         'Parkinsons Disease Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0            # 0=Diabetes, 1=Heart, 2=parkinsons
    )


# ====================================================================
# ===================== DIABETES PREDICTION ==========================================================================================
# ====================================================================


if selected == 'Diabetes Prediction':   #for selecting disease whuch is need to be predicted

    st.title('Diabetes Prediction using ML')

    # Creating input fields in 3 columns
    col1, col2, col3 = st.columns(3)

    # Taking user inputs
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
        
    with col2:
        Age = st.text_input('Age')

    diab_diagnosis = ""


    # When the button is pressed → prediction will happen
    if st.button("Diabetes Test Result"):
        
        
        try:
            # Convert all inputs into numeric form
            inputs = [
                float(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                float(Insulin), float(BMI), float(DiabetesPedigreeFunction), float(Age)
            ]


            # Model prediction
            diab_prediction = diabetes_model.predict([inputs])

            # Result message
            if diab_prediction[0] == 1:
                diab_diagnosis = "⚠ The person is Diabetic"
            else:
                diab_diagnosis = "✔ The person is NOT Diabetic"


        except ValueError:
            # If user enters empty or non-numeric values
            diab_diagnosis = "❌ Please enter valid numeric values in all fields"

    st.success(diab_diagnosis)



# ====================================================================
# ===================== HEART DISEASE PREDICTION =================================================================================
# ====================================================================


if selected == 'Heart Disease Prediction':

    st.title('Heart Disease Prediction using ML')

    # Input fields in 3 columns
    col1, col2, col3 = st.columns(3)

    # Taking user inputs
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain Type')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dl)')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar (> 120 mg/dl)')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')
        
    with col2:
        thalach = st.text_input('Max Heart Rate Achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST Depression Value')
        
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment')
        
    with col3:
        ca = st.text_input('No. of Major Vessels (0–3)')
        
    with col1:
        thal = st.text_input('Thal (0=normal, 1=fixed defect, 2=reversible defect)')

    heart_diagnosis = ""

    if st.button("Heart Disease Result"):
        
        
        try:
            # Convert inputs into numeric values
            inputs = [
                float(age), float(sex), float(cp), float(trestbps), float(chol),
                float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak),
                float(slope), float(ca), float(thal)
            ]


            # Prediction using heart model
            heart_prediction = heart_disease_model.predict([inputs])

            if heart_prediction[0] == 1:
                heart_diagnosis = "⚠ The person has Heart Disease. Please consult a doctor."
            else:
                heart_diagnosis = "✔ The person does NOT have Heart Disease."

        except ValueError:
            heart_diagnosis = "❌ Please enter valid numeric values in all fields"

    st.success(heart_diagnosis)



# ====================================================================
# ===================== PARKINSON'S DISEASE PREDICTION ===========================================================================
# ====================================================================


if selected == 'Parkinsons Disease Prediction':

    st.title("Parkinson's Disease Prediction using ML")

    # Creating 5 column layout for 22 input fields
    col1, col2, col3, col4, col5 = st.columns(5)

    # List of all required input names
    fields = [
        "MDVP:Fo(Hz)",      #Average fundamental frequency (pitch) of the voice in Hertz.
        "MDVP:Fhi(Hz)",     #Maximum fundamental frequency.
        "MDVP:Flo(Hz)",     #Minimum fundamental frequency.
        
        
        "MDVP:Jitter(%)",   # Relative variation in pitch, in percentage.
        "MDVP:Jitter(Abs)", # Absolute variation in pitch.
        "MDVP:RAP",         # (Relative Average Perturbation) – Short-term pitch variation.
        "MDVP:PPQ",         # (Pitch Period Perturbation Quotient) – Measures pitch fluctuations over a few cycles.
        "Jitter:DDP",       # (Difference of Differences of Periods) – Another way to measure pitch instability.
        
        
        "MDVP:Shimmer",     # General measure of amplitude variation
        "MDVP:Shimmer(dB)", # Shimmer measured in decibels.
        "Shimmer:APQ3", # Amplitude variation over 3 cycles.
        "Shimmer:APQ5", # Over 5 cycles.
        "MDVP:APQ",     #Average amplitude variation.
        "Shimmer:DDA",  # Difference of differences in amplitude.
        
        "NHR",          #NHR (Noise-to-Harmonics Ratio) – Ratio of noise to tonal components; higher values indicate breathy/hoarse voice.
        "HNR",          #HNR (Harmonics-to-Noise Ratio) – Inverse of NHR; lower values indicate more noise in voice.
        
        "RPDE",         #RPDE (Recurrence Period Density Entropy) – Measures complexity of speech signal.
        "DFA",          #DFA (Detrended Fluctuation Analysis) – Measures self-similarity in voice.
        "spread1",      
        "spread2",      #spread1 & spread2 – Statistical measures of variability in signal.
        "D2",           #D2 (Correlation Dimension) – Measures complexity of the voice signal.
        "PPE"           #PPE (Pitch Period Entropy) – Entropy in pitch periods; higher means more irregularity.
    ]


    values = []
    index = 0

    # Taking inputs one by one and adding to list
    for f in fields:
        with [col1, col2, col3, col4, col5][index % 5]:
            values.append(st.text_input(f))
        index += 1

    parkinsons_diagnosis = ""
    
    

    if st.button("Parkinson's Disease Result"):
        try:
            # Convert all entered values to numeric
            inputs = list(map(float, values))

            # Prediction
            parkinsons_prediction = parkinsons_model.predict([inputs])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "⚠ The person has Parkinson's Disease."
            else:
                parkinsons_diagnosis = "✔ The person does NOT have Parkinson's Disease."

        except ValueError:
            parkinsons_diagnosis = "❌ Please enter valid numeric values in all fields"

    st.success(parkinsons_diagnosis)






