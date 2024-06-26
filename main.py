from greetings import greetings
from translate import Translator

translator = Translator(to_lang='pt')
for greet in greetings:
    print(f"{translator.translate(greet)}!!!")