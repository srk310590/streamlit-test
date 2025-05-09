import streamlit as st
import time

st.header("This is a sample website")
st.button("Submit")

if st.button("Submit"):
    st.toast("Thank you for visiting the website", icon="🎉")
