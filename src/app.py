import streamlit as st
import pandas as pd
import joblib

clf = joblib.load("model/insurance_model.pkl")

st.text("Made by Silvia Donaire Serrano")

st.title("Prediction medic insurance cost")

age = st.number_input("Age: ", min_value=0, max_value=150)
gender = st.selectbox("Gender: ", ["female", "male"])
bmi = st.slider("BMI: ", min_value=0.0, max_value=100.00)
children = st.number_input("Children: ", min_value=0, max_value=10)
smoker = st.checkbox("Smoker", value=False)
region = st.selectbox("Region: ", ["southwest", "southeast", "northwest", "northeast"])

st.divider()

if st.button("Predict"):
    X = pd.DataFrame([[age, gender, bmi, children, smoker, region]],
                    columns=["age", "sex", "bmi", "children", "smoker", "region"])
    X = X.replace(["male", "female"], [0, 1])
    X = X.replace([False, True], [0, 1])
    X = X.replace(["southwest", "southeast", "northwest", "northeast"], [0, 1, 2, 3])
    
    prediction = clf.predict(X)[0]
    
    st.text(f"The cost of your medic insurance can be {prediction:.2f}$!")