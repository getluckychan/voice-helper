

def voice_checker():
    voice = 'работаем'
    from os import system
    if voice == 'открой хром':
        system("google-chrome")
    elif voice == 'открой телеграм':
        system("telegram-desktop")
    elif voice == 'открой спотифай':
        system("spotify")
    elif voice == 'заглуши':
        system("amixer -D pulse sset Master 0%")
    elif voice == 'включи звук':
        system("amixer -D pulse sset Master 50%")
    else:
        print('something went wrong')


voice_checker()

