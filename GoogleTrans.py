import streamlit as st 
from googletrans import Translator

translator = Translator()

while True:
  word = st.text_input("Give me a word you want me to translate: ")
  word_it = translator.translate(word, src = 'en', dest = 'it')
  st.write(word_it.text)
  st.write("Do you want me to continue? Write 'no' in case not.")
  if word == 'no':
    st.write("OK, Goodbye!")
    break

