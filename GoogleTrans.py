from googletrans import Translator

translator = Translator()

while True:
  word = input("Give me a word you want me to translate: ")
  word_it = translator.translate(word, src = 'en', dest = 'it')
  print(word_it.text)
  print("Do you want me to continue? Write 'no' in case not.")
  if word == 'no':
    print("OK, Goodbye!")
    break

