import speech_recognition as sr
from listener import *
from threading import Thread


# from telegram import *


class VoiceInput:
    def __init__(self):
        self.voice = None

    def on_listen(self, recognizer, audio):
        try:
            voice = recognizer.recognize_google(audio, language='en-US').lower()
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
            print(voice)
            self.voice = voice

            confirming_thread = Thread(target=check_bool(self.voice))
            confirming_thread.start()
            opening_thread = Thread(target=OpenCommand().check(self.voice))
            opening_thread.start()

            def working(cmd):
                checking = {
                    "open": opening_thread.join(5),
                    "volume" or "sound": SoundCommand().check(cmd),
                    "shutdown" or "shut down" or "reboot": confirming_thread.join(5)
                }

            t1 = Thread(target=working(self.voice))
            t1.run()

    def listening(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)

        print('press Enter for closing')
        r.listen_in_background(sr.Microphone(), self.on_listen, phrase_time_limit=6)
        input()


if __name__ == "__main__":
    VoiceInput().listening()
