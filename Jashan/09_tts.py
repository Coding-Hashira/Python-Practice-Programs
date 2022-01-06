# Made by Jashan(Tanjiro)
# -------------Challenge-------------
# Make A Program To convert a text into speech(only in english)
# Source: My Mind LOL

# -------------Code-------------
# imports
from gtts import gTTS
import os
from deep-translator import single_detection

text = input('Enter The Text You Want To Covert Into Audio:\n')

lang = single_detection(text, api_key='c3f945d0809cff67fc859d940fca49fd')

audio = gTTS(text=text, lang=lang)

audio.save('LanguageMaster.mp3')

os.system('LanguageMaster.mp3')