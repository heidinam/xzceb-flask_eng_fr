import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator('QPGmGO_g-cCyNSP9mIrWVXnujkisnEffP7qWdC7MI7Il')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.kr-seo.language-translator.watson.cloud.ibm.com/instances/f7d1c123-965c-46cc-9d02-5d63dfe6f5cb')



def english_to_french(english_text):
    french_text = language_translator.translate(
        english_text,
        model_id='en-fr').get_result()
    return french_text

def french_to_english(french_text):
    english_text = language_translator.translate(
        french_text,
        model_id='fr-en').get_result()
    return english_text
