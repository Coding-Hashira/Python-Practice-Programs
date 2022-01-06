# Made by Jashan(Tanjiro)
# -------------Challenge-------------
# Make A Program To translate Text
# Source: My Mind LOL

# -------------Code-------------
# imports
from deep-translator import GoogleTranslator

text=input('Enter Text You Want To Translate:\n')

toLang = input('Enter Language In Which You Wanna Translate It?\n')

toLang = toLang.lower()

translatedText = GoogleTranslator(source='auto', target=toLang).translate(text=textToTranslate)

print(f'Here\'s Your Translation:\n{translatedText}\n\n')