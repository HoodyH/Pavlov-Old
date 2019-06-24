from core.src.settings import *
import speech_recognition as sr


def speech_to_text(file, language):

    if language == ITA:
        language = 'it-IT'
    else:
        language = 'en-EN'

    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio_data = r.record(source)  # read the entire audio file
        r.pause_threshold = 4.0

    try:
        text = r.recognize_google(audio_data, language=language)
    except Exception as e:
        print(e)
        return ""

    return text
