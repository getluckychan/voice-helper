import speech_recognition as sr
from listener import *
from threading import Thread


# from telegram import *

def check_bool(cmd):
    try:
        SystemCommand().check(cmd)
        checking = {
            "yes": command_need_to_confirm[0],
            "no": "dont say what you dont want"
        }
        print("are u sure")
        print(checking.get(cmd))
        system(checking.get(cmd))
    except IndexError:
        pass


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

            t2 = Thread(target=check_bool(self.voice))
            t2.start()

            def working(cmd):
                checking = {
                    "open": OpenCommand().check(cmd),
                    "volume" or "sound": SoundCommand().check(cmd),
                    "shutdown" or "reboot": t2.join(5)
                }
                return checking.get(cmd)

            t1 = Thread(target=working(self.voice))
            t1.start()

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
