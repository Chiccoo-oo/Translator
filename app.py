from flask import Flask, render_template, request, jsonify, send_file
from googletrans import Translator
from gtts import gTTS
import os
import time

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    text = data.get('text')
    source_lang = data.get('src_lang')

    # Set destination language based on source language
    dest_lang = 'hi' if source_lang == 'bn' else 'bn'
    translated = translator.translate(text, src=source_lang, dest=dest_lang)

    # Generate audio for the translated text
    translated_text = translated.text
    tts = gTTS(text=translated_text, lang=dest_lang)
    
    # Use a unique filename to avoid caching issues
    audio_file = f"translated_audio_{int(time.time())}.mp3"
    tts.save(audio_file)

    return jsonify({'translated_text': translated_text, 'audio_url': f'/{audio_file}'})

@app.route('/<audio_file>')
def get_audio(audio_file):
    return send_file(audio_file, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
