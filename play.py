import speech_recognition as sr
from enum import Enum


def on_listen(recognizer, audio):
    # print('on_listen')
    try:
        voice = recognizer.recognize_google(audio, language='ru-RU').lower()
    except sr.UnknownValueError as e:
        pass
    else:
        command = OpenableCommand(voice)
        command.check(voice)
        # print('Вы сказали:', voice)
        # from os import system
        # if 'открой Chrome' or 'Chrome' in voice:
        #     system("google-chrome")
        # elif 'открой telegram' or 'telegram' in voice:
        #     system("telegram-desktop")
        # elif 'открой спотифай' or 'spotify' in voice:
        #     system("spotify")
        # elif 'заглуши' or 'выключи звук' in voice:
        #     system("amixer -D pulse sset Master 0%")
        # elif 'включи звук' or 'запусти' in voice:
        #     system("amixer -D pulse sset Master 50%")
        # else:
        #     print('something went wrong')


class Command:
    def __init__(self, text):
        self.text = text

    def check(self, text):
        pass


class OpenableCommand(Command):
    open = 'Открыть'

    class SysCommand(Enum):
        chrome = "google-chrome"
        telegram = "telegram-desktop"
        spotify = "spotify"

    def check(self, text):
        text = text.lower()
        for command in self.SysCommand:
            if command.name in text:
                from os import system
                print("Открываю: " + command.name)
                system(command.value)


r = sr.Recognizer()
with sr.Microphone() as source:
    r.pause_threshold = 1
    print('Тихо...')
    r.adjust_for_ambient_noise(source, duration=1)

print('Нажмите Enter для завершения')
print('Говорите...')
r.listen_in_background(sr.Microphone(), on_listen, phrase_time_limit=5)
input()
