import streamlit as st
import joblib
import pandas as pd
import numpy as np

model = joblib.load('Model_Elastic.pkl')
jobs = pd.read_csv('jobs.csv')

st.title("💵 Salary Prediction Model 💵")
st.subheader('🤖 This model uses **ElasticNet Regression** to infer salaries based on job statistics.')
st.markdown('''
            This model was trained using the **Salary Prediction Dataset** from [Kaggle](https://www.kaggle.com). 
    The predictions reflect **Gross Annual Salaries** based on market trends from **North America** and **Europe**.
    
    *Please note: Figures are in USD ($) and represent yearly compensation.*
    ''')
st.markdown('---')


edu_map = {"Bachelor's":1,"Master's":2,'PhD':3}
edu_choice = st.selectbox('Education Level: ',options=list(edu_map.keys()))
edu_value = edu_map[edu_choice]

age = st.number_input('Age: ',min_value=23,max_value=53,value=30)

gender_choice = st.selectbox('Gender: ',options=['Male','Female'])
gender_male = 1 if gender_choice == 'Male' else 0 

job_choice = st.selectbox('Job Title: ', options=jobs['job_title'].unique())
job_mean = jobs[jobs['job_title']==job_choice]['salary_mean'].values[0]

experience = st.number_input('Years of experience: ',min_value=0,max_value=25)

if st.button('Predict Salary',type='primary'):
    input_data = input_data = np.array([[age, gender_male, edu_value, experience, job_mean]])
    prediction = model.predict(input_data)

    st.markdown('---')
    st.subheader(f'Estimated Salary: ${prediction[0]:.2f} per year')
    st.write(f"Analysis completed for a **{age}-year-old** **{job_choice}** holding a **{edu_choice}** degree with **{experience}** years of experience.")
