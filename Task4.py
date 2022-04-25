import streamlit as st 
from googletrans import Translator

translator = Translator()

word = st.text_input("Give me a word you want me to translate: ")
target_l = st.radio("Give me a target language", ("it", "en", "sk", "de")).lower()
target_select = st.selectbox("Give me a target language", ("it", "en", "sk")).lower()


word_it = translator.translate(word, dest = target_l)
st.write(word_it.text)
st.write("Do you want me to continue? Write 'no' in case not.")
if word == 'no':
  st.write("OK, Goodbye!")
