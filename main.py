from micro import micro
from time import sleep


def transcribe_file(speech_file):
    """Transcribe the given audio file asynchronously."""
    from google.cloud import speech

    client = speech.SpeechClient()

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to a 60 seconds audio file.
     Use a GCS file for audio longer than 1 minute.
    """
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="ru-RU",
        audio_channel_count=2,
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        return result.alternatives[0].transcript


def voice_checker():
    voice = transcribe_file(speech_file='/home/ivan/PycharmProjects/pythonProject1/file.wav')
    print(voice)
    from os import system
    if 'Открой Chrome' in voice:
        system("google-chrome")
    elif 'открой телеграм' in voice:
        system("telegram-desktop")
    elif 'открой спотифай' in voice:
        system("spotify")
    elif 'заглуши' in voice:
        system("amixer -D pulse sset Master 0%")
    elif 'Включи звук' in voice:
        system("amixer -D pulse sset Master 50%")
    else:
        print('something went wrong')


while True:
    micro()
    voice_checker()
