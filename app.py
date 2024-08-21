from flask import Flask, render_template, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.json
    bengali_text = data.get('text')
    translated = translator.translate(bengali_text, src='bn', dest='hi')
    return jsonify({'translated_text': translated.text})

if __name__ == '__main__':
    app.run(debug=True)
