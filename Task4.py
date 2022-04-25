import streamlit as st 
from googletrans import Translator

translator = Translator()

word = st.text_input("Give me a word you want me to translate: ")
target_l = st.radio("Give me a target language", ("it", "en", "sk", "de")).lower()

word_it = translator.translate(word, dest = target_l)

st.write(word_it.text)


target_s = st.selectbox("Give me a target language", ("it", "en", "sk")).lower()
target_select = translator.translate(word, dest = target_l)

st.write(target_select.text)





