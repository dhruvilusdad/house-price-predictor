import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model1.pkl")

st.title("🏠 House Price Prediction App")
st.header("Enter House Details Below")
st.markdown("Fill the values and click Predict.")

area = st.number_input("Area (sqft)")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
age = st.number_input("House Age")
location = st.number_input("Location Score(1 to 10)")

if st.button("Predict Price"):
    if area<=0:
        st.error("Area must be grater than 0")
        
    elif bedrooms<=0:
        st.error("Badrooms must be grater than 0")
        
    elif bathrooms<=0:
        st.error("bathrooms must be Gener than 0")
    else:
        input_data = np.array([[area, bedrooms, bathrooms, age, location]])
        prediction = model.predict(input_data)
        st.success(f"Predicted Price: ₹{prediction[0]:,.2f}")