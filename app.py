import streamlit as st
username = st.text_input("Enter Username")
age =st.number_input("Enter your age")
if username==username and age >= 18:
  st.write("Vote")
else:
  st.write("Not vote")
if age >= 120:
  st.write("Not Human")
