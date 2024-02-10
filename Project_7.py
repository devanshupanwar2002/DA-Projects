
import streamlit as st
import pandas as pd
import seaborn as sns
import warnings

#Warnings
warnings.filterwarnings('ignore')

#Title and Subheader
st.title('Data Analysis')
st.subheader('Data Analysis Using Python & Streamlit')

#Upload Dataset
upload=st.file_uploader('Upload Your Dataset (In CSV Format)')
if upload is not None:
    data=pd.read_csv(upload)
    
#Show Dataset
if upload is not None:
    if st.checkbox('Preview Dataset'):
        if st.button('Head'):
            st.write(data.head())
        if st.button('Tail'):
            st.write(data.tail())
            
#Check Dataset of Each Dataset
if upload is not None:
    if st.checkbox('DataType of Each Column'):
        st.text('DataTypes')
        st.write(data.dtypes)
        
#Shape of our Dataset;
if upload is not None:
    data_shape=st.radio('What Dimension do you want to check?',('Rows','Columns'))
    
    if data_shape=='Rows':
        st.text('Number of Rows')
        st.write(data.shape[0])
        
    if data_shape=='Columns':
        st.text('Number of Columns')
        st.write(data.shape[1])
        
#Null values in the Dataset
if upload is not None:
    test=data.isnull().values.any()
    
    if test==True:
        if st.checkbox('Null Values in the Dataset'):
            sns.heatmap(data.isnull())
            st.pyplot()
        else:
            st.success('Congratulation!!!,No Missing Values')
       
#Find Duplicates
if upload is not None:
    test=data.duplicated().any()
    
    if test==True:
        st.warning('This Dataset Contain some Duplicate Value')
        dup=st.selectbox('Do you want to remove duplicates values?',\
                         ('Select one','yes','no'))
        if dup=='Yes':
                data=data.drop_duplicates()
                st.text('Duplicates values are removed')
                
        if dup=='No':
                st.text('Ok No Problem')
            
#Overall Duplicates
if upload is not None:
    if st.checkbox('Summary of the Dataset'):
        st.write(data.describe(include='all'))

#About section
if st.button('About App'):
    st.text('Built With Streamlit')
    st.text('Thanks to Streamlit')
    
#By
if st.checkbox('By'):
    st.success('Devanshu Panwar')    
       
            