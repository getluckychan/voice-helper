import speech_recognition as sr
from listener import *


def working(cmd):
    if "open" in cmd:
        command = OpenCommand()
        command.check(cmd)
    elif "volume" or "sound" in cmd:
        command = SoundCommand()
        command.check(cmd)


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
            working(self.voice)

    def listening(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            print('Тихо...')
            r.adjust_for_ambient_noise(source, duration=1)

        print('Нажмите Enter для завершения')
        print('Говорите...')
        r.listen_in_background(sr.Microphone(), self.on_listen, phrase_time_limit=4)
        input()


if __name__ == "__main__":
    work = VoiceInput()
    work.listening()
