from google.cloud import texttospeech
from translate import translate_word
import os.path

def speak(word, language):
    client = texttospeech.TextToSpeechClient()
    print("Word is "+ word)
    synthesis_input = texttospeech.types.SynthesisInput(text = word)
    voice = texttospeech.types.VoiceSelectionParams(
        language_code = language,
        ssml_gender = texttospeech.enums.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding = texttospeech.enums.AudioEncoding.MP3)
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    # path_name = 'C:/Users/Mayank Kanoria/Documents/Picturlate/resources/'
    # file1 = open(path_name, 'w')
    # file.save(os.path.join(save_path, output.mp3))
    with open('output.mp3', 'wb') as out:
        out.write(response.audio_content)
        print("Sucess!")    

def main():
    speak("Test input for text-to-speech", "en-US")

if __name__ == '__main__':
  main()