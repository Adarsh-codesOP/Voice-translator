from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

app = Flask(__name__)

# Ensure the audio directory exists
if not os.path.exists('static/audio'):
    os.makedirs('static/audio')

def speak(text):
    """Convert text to speech and save it as an MP3 file."""
    tts = gTTS(text=text, lang='kn') 
    audio_file = 'static/audio/translated.mp3'  # Save in the static folder
    tts.save(audio_file)  
    print(f"Audio saved as {audio_file}")

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML form

@app.route('/translate', methods=['POST'])
def translate():
    sentence = request.form['sentence']  # Get the sentence from the form
    if sentence.lower() == "none":
        return jsonify({"translated": "No input provided."})

    trans = GoogleTranslator(source='en', target='kn')
    trans_sen = trans.translate(sentence)
    print(f"Translated: {trans_sen}")
    
    speak(trans_sen)  # Convert translated text to speech
    return jsonify({"translated": trans_sen})  # Return the translated text as JSON

if __name__ == '__main__':
    app.run(debug=True)