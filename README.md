
---

# Voice Translator Project

This project is a **Voice Translator** that takes voice input in one language and provides an audio output in the translated language. The project includes two components:
- A terminal-based application for voice translation.
- A Flask-based web application for voice translation via a web interface.

## Features

- **Voice Input**: Users can provide input through voice in one language.
- **Text Translation**: The voice input is converted to text and then translated into the target language.
- **Audio Output**: The translated text is converted into audio and returned to the user.
- **Terminal Application**: A simple Python script for running the translation in the terminal.
- **Flask Web Application**: A web interface for interacting with the voice translator.

## Requirements

Before running the project, ensure you have the following dependencies installed:
- Python 3.x
- Flask (for the web app)
- SpeechRecognition (for recognizing voice input)
- gTTS (for text-to-speech output)
- Googletrans (for language translation)

### Setting up a Virtual Environment

1. Create a virtual environment using `venv`:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - **On Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **On macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
/voice-translator-project
│
├── /static
│   └── /audio  (This folder is where audio files are saved)
│
├── term.py  (Terminal-based voice translation)
├── webapp.py  (Flask-based web application)
├── requirements.txt  (List of dependencies)
└── README.md  (This file)
```

## Usage

### **1. Terminal-based Translation**

To run the terminal-based voice translator:

1. Navigate to the project folder:
   ```bash
   cd /path/to/voice-translator-project
   ```
2. Run the terminal script:
   ```bash
   python term.py
   ```
   **Note:** There may be some font issues in the terminal for certain languages, resulting in jumbled text. However, you can copy and paste the output into another text editor to check if the translation worked correctly.

### **2. Flask Web Application**

To run the Flask-based voice translator:

1. Ensure you have the necessary dependencies installed:
   ```bash
   pip install -r requirements.txt
   ```
2. Create an `audio` folder inside the `static` folder (if it doesn't exist already) to store the generated audio files:
   ```bash
   mkdir -p static/audio
   ```
3. Run the web application with:
   ```bash
   python webapp.py
   ```
4. Open a web browser and navigate to `http://127.0.0.1:5000/` to use the web-based voice translator.

### **3. Changing Input and Output Languages**

You can change the input and output languages for translation in the Flask app by modifying the following lines in the `webapp.py` file:
- For **text translation**:
  ```python
  tts = gTTS(text=text, lang='ml')  # Change 'ml' to your desired output language
  ```
- For **voice translation**:
  ```python
  trans = GoogleTranslator(source='en', target='ml')  # Change 'en' and 'ml' for input and output languages
  ```

Alternatively, you can create a function within the Flask app to allow users to select their preferred input/output languages dynamically.

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Contributions are always welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).

---
