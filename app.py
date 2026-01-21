import streamlit as st
import pickle
import time

models = {
    'diabetes': pickle.load(open('models_pickle/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('models_pickle/heart_disease.sav', 'rb')),
    'parkinsons': pickle.load(open('models_pickle/parkinsons.sav', 'rb')),
    'lung_cancer': pickle.load(open('models_pickle/lung_cancer.sav', 'rb')),
    'thyroid': pickle.load(open('models_pickle/Thyroid_model.sav', 'rb')),
    'kidney': pickle.load(open('models_pickle/kidney_model.sav', 'rb'))

}

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def main_app():
    st.title("Predictive Health")
    
    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    background_image_url = "https://c4.wallpaperflare.com/wallpaper/697/865/74/abstract-abstraction-biology-chemistry-wallpaper-preview.jpg"  

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url({background_image_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stAppViewContainer"]::before {{
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.7);
    }}
    .stButton > button {{
    background-color: #4CAF50; 
    color: white;
    border: none;
    padding: 10px 20px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.2s;
}}

.stButton > button:hover {{
    background-color: #45a049; 
    transform: scale(1.05); 
    color:gold;
}}

input[type="text"], input[type="number"] {{
    border: 2px solid #ccc;
    border-radius: 4px;
    padding: 10px;
    width: 100%;
    box-sizing: border-box;
    transition: border-color 0.3s;
}}

input[type="text"]:focus, input[type="number"]:focus {{
    border-color: #4CAF50; 
    outline: none; 
}}

    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    if st.session_state.logged_in:
        st.sidebar.success("Welcome!")
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            time.sleep(1)
            st.rerun()
    else:
        st.sidebar.info("Demo login\nUsername: user\nPassword: user@123")

        username = st.sidebar.text_input(
            "Username",
            key="username"
        )

        password = st.sidebar.text_input(
            "Password",
            type="password",
            key="password"
        )

        if st.sidebar.button("Login"):
            if username == "user" and password == "user@123":
                st.session_state.logged_in = True
                st.sidebar.success("Logged in successfully.")
                time.sleep(1)
                st.rerun()
            else:
                st.sidebar.error("Invalid username or password")

    if not st.session_state.logged_in:
        st.warning("Please log in to access the application.")
        return

    selected = st.sidebar.selectbox(
        'Select a Disease to Predict',
        ['Diabetes Prediction',
         'Heart Disease Prediction',
         'Parkinsons Prediction',
         'Lung Cancer Prediction',
         'Hypo-Thyroid Prediction',
         'Chronic Kidney Prediction',
         ]
    )

    def display_input(label, tooltip, key, type="text"):
        if type == "text":
            return st.text_input(label, key=key, help=tooltip)
        elif type == "number":
            return st.number_input(label, key=key, help=tooltip, step=1.0, format="%.2f", value=0.0)

    if selected == 'Diabetes Prediction':
        st.title('Diabetes')
        st.write("Enter the following details to predict diabetes:")
        Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
        Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
        BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
        SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
        Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
        BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
        DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
        Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

        if st.button('Diabetes Test Result'):
            diab_prediction = models['diabetes'].predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            if diab_prediction[0] == 1:
                st.error(diab_diagnosis) 
            else:
                st.success(diab_diagnosis)

    if selected == 'Heart Disease Prediction':
        st.title('Heart Disease')
        st.write("Enter the following details to predict heart disease:")
        age = display_input('Age', 'Enter age of the person', 'age', 'number')
        sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
        cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
        trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
        chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
        fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
        restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
        thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
        exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
        oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
        slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
        ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
        thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

       
        if st.button('Heart Disease Test Result'):
            heart_prediction = models['heart_disease'].predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
            heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
            if heart_prediction[0] == 1:
                st.error(heart_diagnosis) 
            else:
                st.success(heart_diagnosis)

    if selected == "Parkinsons Prediction":
        st.title("Parkinson's Disease")
        st.write("Enter the following details to predict Parkinson's disease:")
        fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
        fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
        flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
        Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
        Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
        RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
        PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
        DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
        Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
        Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
        APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
        APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
        APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
        DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
        NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
        HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
        RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
        DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
        spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
        spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
        D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
        PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

        
        if st.button("Parkinson's Test Result"):
            parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            if parkinsons_prediction[0] == 1:
                st.error(parkinsons_diagnosis) 
            else:
                st.success(parkinsons_diagnosis)

    if selected == "Lung Cancer Prediction":
        st.title("Lung Cancer")
        st.write("Enter the following details to predict lung cancer:")
        GENDER = display_input('Gender (1 = Male; 0 = Female)', 'Enter gender of the person', 'GENDER', 'number')
        AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
        SMOKING = display_input('Smoking (1 = Yes; 0 = No)', 'Enter if the person smokes', 'SMOKING', 'number')
        YELLOW_FINGERS = display_input('Yellow Fingers (1 = Yes; 0 = No)', 'Enter if the person has yellow fingers', 'YELLOW_FINGERS', 'number')
        ANXIETY = display_input('Anxiety (1 = Yes; 0 = No)', 'Enter if the person has anxiety', 'ANXIETY', 'number')
        PEER_PRESSURE = display_input('Peer Pressure (1 = Yes; 0 = No)', 'Enter if the person is under peer pressure', 'PEER_PRESSURE', 'number')
        CHRONIC_DISEASE = display_input('Chronic Disease (1 = Yes; 0 = No)', 'Enter if the person has a chronic disease', 'CHRONIC_DISEASE', 'number')
        FATIGUE = display_input('Fatigue (1 = Yes; 0 = No)', 'Enter if the person experiences fatigue', 'FATIGUE', 'number')
        ALLERGY = display_input('Allergy (1 = Yes; 0 = No)', 'Enter if the person has allergies', 'ALLERGY', 'number')
        WHEEZING = display_input('Wheezing (1 = Yes; 0 = No)', 'Enter if the person experiences wheezing', 'WHEEZING', 'number')
        ALCOHOL_CONSUMING = display_input('Alcohol Consuming (1 = Yes; 0 = No)', 'Enter if the person consumes alcohol', 'ALCOHOL_CONSUMING', 'number')
        COUGHING = display_input('Coughing (1 = Yes; 0 = No)', 'Enter if the person experiences coughing', 'COUGHING', 'number')
        SHORTNESS_OF_BREATH = display_input('Shortness Of Breath (1 = Yes; 0 = No)', 'Enter if the person experiences shortness of breath', 'SHORTNESS_OF_BREATH', 'number')
        SWALLOWING_DIFFICULTY = display_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'Enter if the person has difficulty swallowing', 'SWALLOWING_DIFFICULTY', 'number')
        CHEST_PAIN = display_input('Chest Pain (1 = Yes; 0 = No)', 'Enter if the person experiences chest pain', 'CHEST_PAIN', 'number')

       
        if st.button("Lung Cancer Test Result"):
            lungs_prediction = models['lung_cancer'].predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])
            lungs_diagnosis = "The person has lung cancer disease" if lungs_prediction[0] == 1 else "The person does not have lung cancer disease"
            if lungs_prediction[0] == 1:
                st.error(lungs_diagnosis) 
            else:
                st.success(lungs_diagnosis)

    if selected == "Hypo-Thyroid Prediction":
        st.title("Hypo-Thyroid")
        st.write("Enter the following details to predict hypo-thyroid disease:")
        age = display_input('Age', 'Enter age of the person', 'age', 'number')
        sex = display_input('Sex (1 = Male; 0 = Female)', 'Enter sex of the person', 'sex', 'number')
        on_thyroxine = display_input('On Thyroxine (1 = Yes; 0 = No)', 'Enter if the person is on thyroxine', 'on_thyroxine', 'number')
        tsh = display_input('TSH Level', 'Enter TSH level', 'tsh', 'number')
        t3_measured = display_input('T3 Measured (1 = Yes; 0 = No)', 'Enter if T3 was measured', 't3_measured', 'number')
        t3 = display_input('T3 Level', 'Enter T3 level', 't3', 'number')
        tt4 = display_input('TT4 Level', 'Enter TT4 level', 'tt4', 'number')
       
        if st.button("Thyroid Test Result"):
            thyroid_prediction = models['thyroid'].predict([[age, sex, on_thyroxine, tsh, t3_measured, t3, tt4]])
            thyroid_diagnosis = "The person has Hypo-Thyroid disease" if thyroid_prediction[0] == 1 else "The person does not have Hypo-Thyroid disease"
            if thyroid_prediction[0] == 1:
                st.error(thyroid_diagnosis) 
            else:
                st.success(thyroid_diagnosis)

    if selected == "Chronic Kidney Prediction":
        st.title("Chronic Kidney")
        st.write("Enter the following details to predict Chronic Kidney:")
        AGE = display_input('Age', 'Enter age of the person', 'AGE', 'number')
        BLOODPRESSURE = display_input('Blood Pressure', 'Enter the blood pressure of the person (in mmHg)', 'BLOODPRESSURE', 'number')
        ALBUMIN = display_input('Albumin Levels', 'Enter the albumin levels in urine (g/dL)', 'ALBUMIN', 'number')
        SUGAR = display_input('Blood Sugar', 'Enter the fasting blood sugar level (mg/dL)', 'SUGAR', 'number')
        BLOOD_GLUCOSE_RANDOM = display_input('Random Blood Glucose', 'Enter the random blood glucose level (mg/dL)', 'BLOOD_GLUCOSE_RANDOM', 'number')
        BLOOD_UREA = display_input('Blood Urea', 'Enter the blood urea level (mg/dL)', 'BLOOD_UREA', 'number')
        PACKED_CELL_VOLUME = display_input('Packed Cell Volume', 'Enter the packed cell volume (%)', 'PACKED_CELL_VOLUME', 'number')
        WHITE_BLOOD_CELL = display_input('White Blood Cell Count', 'Enter the white blood cell count (cells/cmm)', 'WHITE_BLOOD_CELL', 'number')
        HYPERTENSION = display_input('Hypertension (1 = Yes; 0 = No)', 'Enter if the person has hypertension', 'HYPERTENSION', 'number')
        DIABETES_MELLITUS = display_input('Diabetes Mellitus (1 = Yes; 0 = No)', 'Enter if the person has diabetes mellitus', 'DIABETES_MELLITUS', 'number')
        CORONARY_ARTERY_DISEASE = display_input('Coronary Artery Disease (1 = Yes; 0 = No)', 'Enter if the person has coronary artery disease', 'CORONARY_ARTERY_DISEASE', 'number')
        ANEMIA = display_input('Anemia (1 = Yes; 0 = No)', 'Enter if the person has anemia', 'ANEMIA', 'number')

        if st.button("Kidney Test Result"):
            kidney_prediction = models['kidney'].predict([[AGE, BLOODPRESSURE, ALBUMIN, SUGAR, BLOOD_GLUCOSE_RANDOM, BLOOD_UREA, PACKED_CELL_VOLUME,WHITE_BLOOD_CELL,HYPERTENSION,DIABETES_MELLITUS,CORONARY_ARTERY_DISEASE,ANEMIA]])
            kidney_diagnosis = "The person has Chronic-Kidney Disease" if kidney_prediction[0] == 1 else "The person does not have Chronic-Kidney Disease"
            if kidney_prediction[0] == 1:
                st.error(kidney_diagnosis) 
            else:
                st.success(kidney_diagnosis)

main_app()
