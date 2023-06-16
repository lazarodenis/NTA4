import streamlit as st
import random

st.title('guess the number game')
number = random.randint(1,100)
guess = st.number_input("enter a number(between 1 and 100):,min_value=1,max_value=100)
if st.button("make a guess!"):
                        if guess > number:
                        st.write("too high! try a smaller number.")
                        elif guess < number:
                        st.write("too low! try a larger number.")
                        else:
                        st.write("congratulation! you have guess the number correctly.")
                        
