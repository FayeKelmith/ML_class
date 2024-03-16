import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st 



room_occupancy = pd.read_csv("./dataset/occupancy_est.csv")
# data = pd.DataFrame(room_occupancy)

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
    
    st.warning("Our dataset is 'mostly' clean. We have no missing values. We will proceed to visualize our data. We only have to average out the temperature values. So, we will proceed to do that.")
    
    room_occupancy["Temperature"] = room_occupancy[["S1_Temp","S2_Temp","S3_Temp","S4_Temp"]].mean(axis=1)
    
    room_occupancy.head()
    st.header("Data Visualization")
    
    st.title("Let's visualize the distribution of our data")
    
    st.divider()
    
    st.subheader("Temperature Distribution")
    
    
    fig, ax = plt.subplots()
    sns.lineplot(y=room_occupancy['Temperature'],x=room_occupancy["Room_Occupancy_Count"],ax=ax)
    st.pyplot(fig)
    
    st.info("We observe a direct correlation between temperature and the number of people present in the room.")
    
    st.divider()
    
    st.subheader("PIR Signal Distribution")
    
    fig1, ax1 = plt.subplots()
    sns.barplot(x=room_occupancy["S6_PIR"],y=room_occupancy["Room_Occupancy_Count"],ax=ax1)
    st.pyplot(fig1)
    
    st.info("We observe that the PIR signals the presence of someone in the room when the count is greater than or equal to 1. Double validation of the correctness of our dataset.")
    
    st.success("Aren't you curious what CO2 levels, Light and Sound levels tell us about the room occupancy? 🤔 Let's dig in!")
    
    st.divider()
    
    fig2, ax2 = plt.subplots()
    sns.lineplot(y=room_occupancy['S5_CO2'],x=room_occupancy["Room_Occupancy_Count"],ax=ax2)
    st.pyplot(fig2)
    
    st.info("Voila! The more people in the room, the higher the CO2 levels. Unless we've got corpses amongst us! 😂")
    
    st.divider()
    
    st.subheader("Light Distribution")
    
    #plot four subplots in one figure each for s1_light, s2_light, s3_light, s4_light
    
    cols = ["S1_Light","S2_Light","S3_Light","S4_Light"]
    fig3, ax3 = plt.subplots(2,2,figsize=(10,10))
    for i in range(2):
        for j in range(2):
            sns.lineplot(y=room_occupancy[cols[i*2+j]],x=room_occupancy["Room_Occupancy_Count"],ax=ax3[i,j])
    st.pyplot(fig3)
    
    st.info("Ion Know about you, but I can't make sense of this data. But I'm sure it's important. 😅")
    
    st.divider()
    
    st.subheader("Sound Distribution")
    
    sound_cols = ["S1_Sound","S2_Sound","S3_Sound","S4_Sound"]
    fig4, ax4 = plt.subplots(2,2,figsize=(10,10))
    for i in range(2):
        for j in range(2):
            sns.lineplot(y=room_occupancy[sound_cols[i*2+j]],x=room_occupancy["Room_Occupancy_Count"],ax=ax4[i,j])
            
    st.pyplot(fig4)
    st.info("Yep! Noise makers! Can't keep your mouths shut! 😃")
    
    st.title("Miscellaneous")
    
    st.text("This data was collected in 7 days as follows:")
    
    #bar plot for date
    fig5, ax5 = plt.subplots()
    room_occupancy["Date"].value_counts().plot(kind='line', ax=ax5)
    ax5.set_xticklabels(ax5.get_xticklabels(), rotation=-45)
    st.pyplot(fig5)
    
    st.divider()
    
    st.subheader("Before we close this chapter, how does the date relate to the number of people in the room?")
    
    count_per_day = room_occupancy.groupby("Date")["Room_Occupancy_Count"].sum()
    count_per_jour = room_occupancy["Date"].value_counts()
    
    fig6, ax6 = plt.subplots()
    sns.barplot(x=count_per_jour.index,y=count_per_jour.values,ax=ax6)
    ax6.set_xticklabels(ax6.get_xticklabels(), rotation=-45)
    st.pyplot(fig6)
    
    st.info("Sans Commentaire! 🤐")
    
    
    st.header("Ait! we're done here! 🥂")
    
    
    
with model:
    st.write("Let's test our model")