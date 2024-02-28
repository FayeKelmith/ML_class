import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 



room_occupancy = pd.read_csv("./dataset/occupancy_est.csv")

st.title("Room Occupancy Model")

st.subheader("This project has been created to predict room occupancy. It is segmented into two parts: Exploratory Data Analysis and Model in Action.")
st.divider()

eda,model = st.tabs(["Exploratory Data Analysis","Model in Action"])

with eda:
    st.header("Exploratory Data Analysis")

    st.subheader("About Dataset")
    
    st.info("The experimental testbed for occupancy estimation was deployed in a 6m Ã— 4.6m room. The setup consisted of 7 sensor nodes and one edge node in a star configuration with the sensor nodes transmitting data to the edge every 30s using wireless transceivers. No HVAC systems were in use while the dataset was being collected.")
    
    st.subheader("Dataset Attributes")
    

    st.text("Date and Time ⏲ ")

    st.text("Temperature in Celsius 🌡")

    st.text("Light: In Lux 🔥")

    st.text("Sound: In Volts(amplifier output read by ADC) 🔈")

    st.text("CO2: In PPM 🌋")

    st.text("CO2 Slope: Slope of CO2 values taken in a sliding window 🌬")
  
    st.text("PIR: Binary value conveying motion detection 🚶‍♂️")
 
    st.text("Room_Occupancy_Count: Ground Truth ⚖")
    
    st.divider()
    
    st.subheader("Our data looks like this")
    
    st.dataframe(room_occupancy.head(5))
    
    st.error("Clearly our dataset needs some cleaning. We have redundant columns( Light, Sound and PIR) let's fix that.")
    
    st.header("Experimental")
    
    st.bar_chart(room_occupancy["Room_Occupancy_Count"])
 
    
with model:
    st.write("Let's test our model")