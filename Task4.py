import streamlit as st 
from googletrans import Translator

translator = Translator()

word = st.text_input("Give me a word you want me to translate: ")
target_l = st.radio("Give me a target language", ("it", "en", "sk", "de")).lower()
st.write(word_it.text)
target_select = st.selectbox("Give me a target language", ("it", "en", "sk")).lower()
st.write(target_select.text)



word_it = translator.translate(word, dest = target_l)

