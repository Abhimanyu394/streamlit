import streamlit as st

st.title('Machine learning app')

st.write('Hello world!')
st.info("This is my ml app")
df=pd.read_csv('train.csv')
df
