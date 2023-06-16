import streamlit as st
import random

st.title('guess the number game')

#generate a random number between 1 and 100
number = random.randint(1,100)

guess = st.number_input("enter a number(between 1 and 100):,min_value=1,max_value=100)
                        
if st.button("make a guess!"):
    if guess > number:
         st.write("Too high! Try a smaller number.")
    elif guess < number:
         st.write("Too low try a larger number.")
    else:
         st.write("Congratulation! you have guessed the number correctly.")
