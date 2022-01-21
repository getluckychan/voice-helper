import speech_recognition as sr
from speech_recognition import Microphone

m = None
for i, microphone_name in enumerate(Microphone.list_microphone_names()):
    print(microphone_name)