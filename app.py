from aitextgen import aitextgen
# importing the open-source library
import streamlit as st
# importing streamlit for front-end

ai = aitextgen(model_folder="trained_model")
# Specifying the fine-tuned model location

input_text = st.text_input(label="Enter your initial text", value="Love")
# Taking the input from user

if st.button('Generate'):
    poem_text =  ai.generate_one(prompt = input_text, max_length=50)
    # Generating the text
    st.text(poem_text)
    # Displaying the text
