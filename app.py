from aitextgen import aitextgen
import json
import streamlit as st
import os
import re
from collections import defaultdict as df
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout, Bidirectional
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import regularizers
import tensorflow.keras.utils as ku 
from tensorflow import keras
import numpy as np
import pickle
# importing the open-source library
# importing streamlit for front-end
st.title('Hinglish Poetry')

option_name = ["Hindi","English"]
option = st.sidebar.radio(
     'Select a language',
    option_name)

if option == 'Hindi':
    with open('trained_model_hindi/tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    with open('trained_model_hindi/idx_to_word.pickle', 'rb') as handle:
        idx_to_word = pickle.load(handle)

    max_seq = 43


    model = keras.models.load_model('trained_model_hindi/hindipoet32_5.h5')


    def gen_poem(model, length, w2i, i2w, start = ' ', lines = 1):
        ipseq = [w2i[s] for s in start if s in w2i]

        lsc = 0
        while lsc<lines:
            ip = np.array(pad_sequences([ipseq], maxlen=length, padding='pre'))

            w = model.predict(ip)[0]
            w = np.argmax(w)
            if i2w[w].strip() == '<sep>':
                lsc+=1
            start+=' '+ i2w[w]
            ipseq.append(w)
        for i in start.split('<sep>'):
            st.text(i.strip())



    input_text = st.text_input(label="Enter your initial text", value="जन्नत")

    int_val = st.number_input('Number of lines', min_value=5, max_value=12, value=8, step=1)
    if st.button('Generate'):
    

        gen_poem(model, max_seq, tokenizer, idx_to_word, input_text, int_val+2)

elif option == 'English':
    ai = aitextgen(model_folder="trained_model")
    # Specifying the fine-tuned model location

    input_text = st.text_input(label="Enter your initial text", value="Love")
    # Taking the input from user

    if st.button('Generate'):
        poem_text =  ai.generate_one(prompt = input_text, max_length=50, )
        # Generating the text
        st.text(poem_text)
        # Displaying the text

