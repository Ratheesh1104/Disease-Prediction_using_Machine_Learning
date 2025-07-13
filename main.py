import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# set page configuration
st.set_page_config(page_title='Health Assistant',
                   layout = 'wide',
                   page_icon = "🩺")

#getting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# load the model
diabetes_model = pickle.load(open(f'{working_dir}/models/diabetes_model.sav', 'rb'))

heart_model = pickle.load(open(f'{working_dir}/models/heart_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu("Disease Prediction System",
                           
                           ["Diabetes Prediction",
                            "Heart Disease Prediction",
                            "Parkinsons Disease Prediction"],
                            menu_icon = "hospital-fill",
                            icons = ["activity", "heart", "person"],
                            default_index = 0)
    
# diabetes prediction page
if selected == "Diabetes Prediction":

    # page title 
    st.title("Diabetes Prediction uisng ML")

    # getting the input
    col1, col2, col3 = st.columns(3)

    with col1:
        Pragnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level")

    with col3:
        BloodPressure = st.text_input("Blood Pressure Value")

    with col1:
        SkinThickness = st.text_input("Skin Thickness Value")

    with col2:
        Insulin = st.text_input("Insulin Level")
    
    with col3:
        BMI = st.text_input("BMI Value")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")

    with col2:
        Age = st.text_input("Age of the Person")

    # code for prediciton
    diab_diagnosis = ''

    # creating a button for prediction
    if st.button("Diabetes Test Result"):

        user_input = [Pragnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = "The person is Diabetic"
        else:
            diab_diagnosis = "The person is Not Diabetic"

    st.success(diab_diagnosis)

# heart disease prediction page
if selected == "Heart Disease Prediction":

    # page title
    st.title("Heart Disease Prediction using ML")

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input("Age")

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input("Chest Pain Type")

    with col1:
        trestbps = st.text_input("Resting Blood Pressure")

    with col2:
        chol = st.text_input("Cholesterol")

    with col3:
        fbs = st.text_input("Fasting Blood Sugar")

    with col1:
        restecg = st.text_input("Resting Electrocardiographic Results")

    with col2:
        thalach = st.text_input("Maximum Heart Rate Achieved")

    with col3:
        exang = st.text_input("Exercise Induced Angina")

    with col1:
        oldpeak = st.text_input("Oldpeak")

    with col2:
        slope = st.text_input("Slope of the Peak Exercise ST Segment")

    with col3:
        ca = st.text_input("Number of Major Vessels Colored by Fluoroscopy")

    with col1:
        thal = st.text_input("thal: 0 = normal defected; 1 = fixed defect; 2 = reversable defect")

    # code for prediction
    heart_diagnosis = ''

    # creating the button for prediction
    if st.button ("Heart Disease Test Result"):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_model.predict([user_input])

        if heart_prediction[0]== 1:
            heart_diagnosis = "The person is having Heart Disease"
        else:
            heart_diagnosis = "The person does not have Heart Disease"

    st.success(heart_diagnosis)

# parkinsons disease prediction page
if selected == "Parkinsons Disease Prediction":

    # page title 
    st.title("Parkinsons Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")

    with col4:
        Jitter_percent = st.text_input("MDVP:Jitter(%)")

    with col5:
        Jitter_Abs = st.text_input("MDVP:Jitter(Abs)")

    with col1:
        RAP = st.text_input("MDVP:RAP")

    with col2:
        PPQ = st.text_input("MDVP:PPQ")

    with col3:
        DDP = st.text_input("Jitter:DDP")

    with col4:
        Shimmer = st.text_input("MDVP:Shimmer")

    with col5:
        Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")  

    with col1:
        APQ3 = st.text_input("Shimmer:APQ3")

    with col2:
        APQ5 = st.text_input("Shimmer:APQ5")

    with col3:
        APQ = st.text_input("MDVP:APQ")

    with col4:
        DDA = st.text_input("Shimmer:DDA")  
    
    with col5:
        NHR = st.text_input("NHR")

    with col1:
        HNR = st.text_input("HNR")

    with col2:
        RPDE = st.text_input("RPDE")

    with col3:
        DFA = st.text_input("DFA")

    with col4:
        spread1 = st.text_input("spread1")

    with col5:
        spread2 = st.text_input("spread2")

    with col1:
        D2 = st.text_input("D2")

    with col2:
        PPE = st.text_input("PPE")

    # code for prediction
    parkinsons_diagnosis = ''

    # button for prediction
    if st.button("Parkinsons Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB,
                      APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person is having Parkinsons Disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinsons Disease"

    st.success(parkinsons_diagnosis)