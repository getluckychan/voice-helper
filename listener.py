from enum import Enum
from abc import ABC, abstractmethod
from os import system


command_need_to_confirm = []


class Command(ABC):
    @abstractmethod
    def check(self, text):
        pass


class OpenCommand(Command):
    class SysCommand(Enum):
        chrome = "google-chrome"
        telegram = "telegram-desktop"
        spotify = "spotify"

    def check(self, text):
        text = text.lower()
        for command in self.SysCommand:
            if command.name in text:
                print("opening: " + command.name)
                system(command.value)


class SoundCommand(Command):
    class SysCommand(Enum):
        off = "amixer set Master mute"
        on = "amixer set Master unmute\n" \
             "amixer set Headphone unmute\n" \
             "amixer set Speaker unmute"
        increase = "amixer -D pulse sset Master 20%+"
        decrease = "amixer -D pulse sset Master 20%-"

    def check(self, text):
        text = text.lower()
        for command in self.SysCommand:
            if command.name in text:
                print("working: " + command.name)
                system(command.value)


class SystemCommand(Command):
    class SysCommand(Enum):
        shutdown = "poweroff"
        reboot = "reboot"

    def check(self, text):
        com = text.split()
        com = ''.join(com)
        for command in self.SysCommand:
            if command.name in com:
                command_need_to_confirm.append(command.value)
                pass


def check_bool(cmd):
    try:
        SystemCommand().check(cmd)
        checking = {
            "yes": f'{command_need_to_confirm[0]}',
            "no": "dont say what you dont want"
        }
        print("are u sure")
        try:
            system(checking.get(cmd))
        except TypeError:
            pass
        else:
            print("don`t say what you want")
    except IndexError:
        pass
