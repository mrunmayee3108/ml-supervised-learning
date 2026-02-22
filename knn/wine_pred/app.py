import streamlit as st
import requests 
st.set_page_config(page_title="Wine class Prediction", page_icon="🍷", layout="wide")
st.title("🍷 Wine Class Prediction 🍷")
st.write("This app predicts the class of wine based on its chemical properties")
st.write("Please enter the chemical properties of the wine below:")
alcohol = st.number_input("Alcohol: ")
malic_acid = st.number_input("Malic Acid: ")
ash = st.number_input("Ash: ")
alcalinity_of_ash = st.number_input("Alcalinity of Ash: ")
magnesium = st.number_input("Magnesium: ")
total_phenols = st.number_input("Total Phenols: ")
flavanoids = st.number_input("Flavanoids: ")
nonflavanoid_phenols = st.number_input("Nonflavanoid Phenols: ")
proanthocyanins = st.number_input("Proanthocyanins: ")
color_intensity = st.number_input("Color Intensity: ")
hue = st.number_input("Hue: ")
od280_od315_of_diluted_wines = st.number_input("OD280/OD315 of Diluted Wines: ")
proline = st.number_input("Proline: ")

if st.button("Predict"):
    data = {
        "alcohol": alcohol,
        "malic_acid": malic_acid,
        "ash": ash,
        "alcalinity_of_ash": alcalinity_of_ash,
        "magnesium": magnesium,
        "total_phenols": total_phenols,
        "flavanoids": flavanoids,
        "nonflavanoid_phenols": nonflavanoid_phenols,
        "proanthocyanins": proanthocyanins,
        "color_intensity": color_intensity,
        "hue": hue,
        "od280_od315_of_diluted_wines": od280_od315_of_diluted_wines,
        "proline": proline
    }
    response = requests.post("http://localhost:8000/predict", json=data)
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"The predicted class of wine is: {prediction}")
    else:
        st.error("Error in prediction. Please try again.")