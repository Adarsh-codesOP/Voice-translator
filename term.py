from deep_translator import GoogleTranslator
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query

def Translate():
	speak("what I should Translate??")
	sentence = takeCommand()
	trans = GoogleTranslator(source='en', target='kn')
	trans_sen = trans.translate(sentence)
	print(trans_sen)
	speak(trans_sen)

def translate_text(sentence):
    translated = GoogleTranslator(source='en', target='kn').translate(sentence)
    return translated

Translate()
