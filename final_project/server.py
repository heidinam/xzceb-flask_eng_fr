from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    def english_to_french(english_text):
    french_text = language_translator.translate(
        english_text,
        model_id='en-fr').get_result()
    return french_text
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    def french_to_english(french_text):
    english_text = language_translator.translate(
        french_text,
        model_id='fr-en').get_result()
    return english_text
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    print("What text should I translate for you?")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
