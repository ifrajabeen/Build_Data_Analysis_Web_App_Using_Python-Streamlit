import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
#Title & Subheader
st.title("DATA ANALYSIS")
st.subheader("Data Analysis Using Python & Streamlit")
# Upload Dataset
upload = st.file_uploader("Upload Your Dataset (In CSV Format)")
if upload is not None:
  data = pd.read_csv(upload)
#Show Dataset
if st.checkbox("Preview Dataset"):
  if st.button("Head"):
    st.write(data.head())
  if st.button("Tail"):
    st.write(data.tail()) 

# Check DataType of each Column
if upload is not None:
  if st.checkbox("DataType of each Column"):
    st.text("Datatypes")
    st.write(data.dtypes)
# Find shape of or dataset(NUmber of columns/ Number of Rows)
if upload is not None:
  data_shape = st.radio("What Dimension Do you want to check?",('Rows','Columns'))
  if data_shape == 'Rows':
    st.text("Number of Rows")
    st.write(data.shape[0])
  if data_shape == 'Columns':
    st.text("Number of Columns")
    st.write(data.shape[1])

#Find NUll Values in the dataset
if upload is not None:
  test=data.isnull().values.any()
  if test==True:
    if st.checkbox("Null Values in the dataset"):
      fig, ax = plt.subplots(figsize=(10,6))
      sns.heatmap(data.isnull(), ax=ax, cbar=False, cmap="viridis")
      st.pyplot(fig)
  else:
    st.success("Congratulations!!! , No Missing Values in this dataset")

#Find Duplicate Values in the dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This Dataset Contains Some Duplicate Values")
        dup=st.selectbox("Do You Want to Remove Duplicate Values?",
                         ("Select One","Yes","No"))
        if dup=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate Values are Removed")
        if dup=="No":
            st.text("Ok No Problem")
    else:
      st.success("This Dataset has no Duplicated values")  
# Get Overall Statistics
if upload is not None:
  if st.checkbox("SUmmary of the dataset"):
    st.write(data.describe(include='all'))

# About Section
if st.button("About App"):
  st.text("Built with Streamlit")
  st.text("Thanks to streamlit")

#BY
if st.checkbox("BY"):
  st.success("Ifra Jabeen")