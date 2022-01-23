import speech_recognition as sr

voice_list = []


class VoiceInput:

    def __init__(self):
        self.voice = ""

    def on_listen(self, recognizer, audio):
        try:
            voice = recognizer.recognize_google(audio, language='en-US').lower()
        except sr.UnknownValueError:
            self.voice = ""
            pass
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        else:
            self.voice = voice
            pass
            # confirming_thread = Thread(target=check_bool(self.voice))
            #
            # opening_thread = Thread(target=OpenCommand().check(self.voice))
            #
            # sound_thread = Thread(target=SoundCommand().check(self.voice))

    def listening(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=1)
        r.listen_in_background(sr.Microphone(), self.on_listen, phrase_time_limit=6)
        if self.voice == "":
            self.listening()
        else:
            voice_list.append(str(self.voice))


# [ord(c) for c in VoiceInput().listening()]
def converting():
    VoiceInput().listening()
    return voice_list[0]
