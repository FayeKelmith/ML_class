import streamlit as st 
import pandas as pd

st.title('Housing Data')

# Load data
df = pd.read_csv('./housing_data.csv')

st.write(df)



# fix this streamlit application and make project here. 