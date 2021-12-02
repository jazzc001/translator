from translate import Translator
translator= Translator(to_lang="ja")


answer = input("What do you want to translate? ")
translation = translator.translate(str(answer))
print(f"The translatetion is:  {translation}")