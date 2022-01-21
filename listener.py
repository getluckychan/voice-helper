from enum import Enum
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def check(self, text):
        pass


class OpenCommand(Command):
    open = 'open'

    class SysCommand(Enum):
        chrome = "google-chrome"
        telegram = "telegram-desktop"
        spotify = "spotify"

    def check(self, text):
        text = text.lower()
        for command in self.SysCommand:
            if command.name in text:
                from os import system
                print("opening: " + command.name)
                system(command.value)


class SoundCommand(Command):
    sound = "sound"

    class SysCommand(Enum):
        mute = "amixer -c 0 set Mic mute"
        unmute = "amixer -c 0 set Mic unmute"

    def check(self, text):
        text = text.lower()
        for command in self.SysCommand:
            if command.name in text:
                from os import system
                print("working: " + command.name)
                system(command.value)
