import streamlit as st
from sklearn.preprocessing import StandardScaler
import pickle
import pandas as pd

with open('Random Classifier Model.pkl','rb') as file:
    model=pickle.load(file)
with open('Standard_Scaler_Features.pkl','rb') as file:
    scaler=pickle.load(file)
with open('labelencoded_targetclass.pkl','rb') as file:
    label_encoder=pickle.load(file)


st.title(':red[Smart Crop Recommendation]')
st.write('Enter the Soil Composition and Enviornmental Conditions as mentioned below and Values must be greater or equal to zero')
N=st.number_input('Level of Nitrogen Content in the Soil',min_value=0)
P=st.number_input('Level of Phosphorus Content in the Soil',min_value=0)
K=st.number_input('Level of Pottasium Content in the Soil',min_value=0)
Tem=st.number_input('Enviornmental Temperature in degree Celcius',min_value=0)
humidity=st.number_input('Relative Humidity in %',min_value=0)
pH=st.number_input('Soil pH Level',min_value=0)
rainfall=st.number_input('Amount of rainfall in Millimeter',min_value=0)
# 'N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'
#prepare the input data into Dataframe format
if st.button('Recommended Crop'):
    try:
        input_data=pd.DataFrame({
                    'N' :[N],
                    'P' :[P],
                    'K':[K],
                    'temperature':[Tem],
                    'humidity':[humidity],
                    'ph':[pH],
                    'rainfall':[rainfall]

                })
        input_data_scaled=scaler.transform(input_data)
        pred_encoded=model.predict(input_data_scaled)
        pred_label=label_encoder.inverse_transform(pred_encoded)


        st.success(f'Recommended Crop based on soil composition and enviornmental condition is {pred_label}')
    except Exception as e:
        st.error(f'An error is occured  {e}')
        
