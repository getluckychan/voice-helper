from enum import Enum
from os import system


class OpenCommand(Enum):
    chrome = "google-chrome"
    telegram = "telegram-desktop"
    spotify = "spotify"


def check_open(string):
    text = string.value
    for cmd in text.split(" "):
        checking = ["open"
                    ]
        if cmd in checking:
            for command in OpenCommand:
                if command.name in text:
                    print("opening: " + command.name)
                    system(command.value)


class SoundCommand(Enum):
    off = "amixer set Master mute"
    on = "amixer set Master unmute\n" \
         "amixer set Headphone unmute\n" \
         "amixer set Speaker unmute"
    increase = "amixer -D pulse sset Master 20%+"
    decrease = "amixer -D pulse sset Master 20%-"


def check_sound(string):
    text = string.value
    for cmd in text.split(" "):
        checking = ["volume",
                    "sound"
                    ]
        if cmd in checking:
            for command in SoundCommand:
                if command.name in text:
                    print("working: " + command.name)
                    system(command.value)


command_need_to_confirm = []


class SysCommand(Enum):
    shutdown = "poweroff"
    reboot = "reboot"


def check_sys(string):
    text = string.value
    com = text.split()
    com = ''.join(com)
    for command in SysCommand:
        if command.name in com:
            command_need_to_confirm.append(command.value)
            pass


def check_bool(text):
    try:
        checking = {
            "yes": f'{command_need_to_confirm[0]}',
            "no": "dont say what you dont want"
        }
        print("are u sure")
        try:
            system(checking.get(text))
            print("don`t say what you want")
        except TypeError:
            pass
    except IndexError:
        pass
