# Made by Jashan(Tanjiro)
# -------------Challenge-------------
# Make A Program To detect language in a Text
# Source: My Mind LOL

# -------------Code-------------
# imports
from deep-translator import single_detection, GoogleTranslator

detectText = input('Enter Your Text:\n')

lang = single_detection(detectText, api_key='c3f945d0809cff67fc859d940fca49fd')

langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)

for k, v in langs_dict.items():
    if v==lang:
        print(f'This Text Is Written In {k.capitalize}')