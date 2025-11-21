import streamlit as st
import pandas as pd

st.title('Machine learning app')

st.write('Hello world!')
st.info("This is my ml app")
df=pd.read_csv('train.csv')
df
