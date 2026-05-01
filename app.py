import streamlit as st
from src.pipeline.predict_pipeline import PredictionPipeline

st.title("Climate Visibility Prediction")

st.write("Enter weather details below:")

# Inputs
drybulb = st.number_input("Dry Bulb Temperature", value=25.0)
humidity = st.number_input("Relative Humidity", value=60)
wind_speed = st.number_input("Wind Speed", value=5.0)
wind_dir = st.number_input("Wind Direction", value=180)
pressure = st.number_input("Sea Level Pressure", value=1013)
year = st.number_input("Year", value=2024)
month = st.number_input("Month", value=4)
hour = st.number_input("Hour", value=10)

# Prediction button
if st.button("Predict"):

    pipeline = PredictionPipeline()

    data = {
        "DRYBULBTEMPF": drybulb,
        "RelativeHumidity": humidity,
        "WindSpeed": wind_speed,
        "WindDirection": wind_dir,
        "SeaLevelPressure": pressure,
        "year": year,
        "month": month,
        "hour": hour
    }

    result = pipeline.predict(data)

    st.success(f"Predicted Visibility: {result}")