import speech_recognition as sr
from listener import *
from threading import Thread
from os import system


def working(cmd):
    checking = {
        "open": OpenCommand().check(cmd),
        "shutdown" or "reboot": SystemCommand().check(cmd),
        "volume" or "sound": SoundCommand().check(cmd)
    }
    return checking.get(cmd)


def confirm(cmd):
    return SystemCommand().check_bool(cmd)


class VoiceInput:
    def __init__(self):
        self.voice = None

    def on_listen(self, recognizer, audio):
        try:
            voice = recognizer.recognize_google(audio, language='en-US').lower()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
            print(voice)
            self.voice = voice
            func = working(self.voice)
            func1 = confirm(self.voice)
            Thread(target=func).start()
            Thread(target=func1).start()

    def listening(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            print('Тихо...')
            r.adjust_for_ambient_noise(source, duration=1)

        print('Нажмите Enter для завершения')
        print('Говорите...')
        r.listen_in_background(sr.Microphone(), self.on_listen, phrase_time_limit=6)
        input()


if __name__ == "__main__":
    VoiceInput().listening()
