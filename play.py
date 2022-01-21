import speech_recognition as sr
from listener import *


def on_listen(recognizer, audio):
    # print('on_listen')
    try:
        voice = recognizer.recognize_google(audio, language='en-US').lower()
    except sr.UnknownValueError as e:
        pass
    else:
        print(voice)
        if "open" in voice:
            command = OpenCommand()
            command.check(voice)
        elif "sound" in voice:
            command = SoundCommand()
            command.check(voice)


r = sr.Recognizer()
with sr.Microphone() as source:
    r.pause_threshold = 1
    print('Тихо...')
    r.adjust_for_ambient_noise(source, duration=1)

print('Нажмите Enter для завершения')
print('Говорите...')
r.listen_in_background(sr.Microphone(), on_listen, phrase_time_limit=5)
input()
