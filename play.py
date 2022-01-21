import speech_recognition as sr
from listener import *


# def on_listen(recognizer, audio):
#     # print('on_listen')
#     try:
#         voice = recognizer.recognize_google(audio, language='en-US').lower()
#     except sr.UnknownValueError as e:
#         pass
#     else:
#         return voice
#
#
# def working():
#     if "open" in voice:
#         command = OpenCommand()
#         command.check(voice)
#     elif "volume" or "sound" in voice:
#         command = SoundCommand()
#         command.check(voice)
#
#
# r = sr.Recognizer()
# with sr.Microphone() as source:
#     r.pause_threshold = 1
#     print('Тихо...')
#     r.adjust_for_ambient_noise(source, duration=1)
#
# print('Нажмите Enter для завершения')
# print('Говорите...')
# r.listen_in_background(sr.Microphone(), on_listen, phrase_time_limit=4)
# input()


class VoiceInput:
    def __init__(self, r):
        self.r = r
        self.voice = None

    def on_listen(self, recognizer, audio):
        # print('on_listen')
        try:
            voice = recognizer.recognize_google(audio, language='en-US').lower()
        except sr.UnknownValueError as e:
            pass
        else:
            print(voice)
            self.voice = voice
            return self.voice

    def listening(self):
        # with sr.Microphone() as source:
        #     r.pause_threshold = 1
        #     print('Тихо...')
        #     r.adjust_for_ambient_noise(source, duration=1)
        print('Нажмите Enter для завершения')
        print('Говорите...')
        self.r.listen_in_background(sr.Microphone(), source=sr.AudioSource, callback=self.on_listen, phrase_time_limit=4)
        input()

    def working(self):
        if "open" in self.voice:
            command = OpenCommand()
            command.check(self.voice)
        elif "volume" or "sound" in self.voice:
            command = SoundCommand()
            command.check(self.voice)


work = VoiceInput(sr.Recognizer)
work.listening()
work.working()
