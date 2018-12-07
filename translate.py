#Function to use input word and translate into chosen language
#Uses language_codes.py to get the language code

#install gcp translate
#get API key and set to path
from google.cloud import translate
translate_client = translate.Client()
from language_codes import get_code

#word is the text to be translated
#langauage is the language to be translated in

def translate_word(word, language):
    language_code = get_code(language)
    translation = translate_client.translate(word, target_language = language_code)
    print(word + " translates to " + translation['translatedText'])
    values = {'orig': word, 'text': translation['translatedText']} 
    return values

# def main():
#     translate_word("Hello", 'fr')

# if __name__ == '__main__':
#   main()
