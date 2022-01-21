from enum import Enum
from abc import ABC, abstractmethod
from os import system


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
        text = text.lower()
        for command in self.SysCommand:
            if command.name in text:
                print("Do u really want to do it?\n"
                      "press enter if yes")
                if input() == "\n":
                    print("working: " + command.name)
                    system(command.value)
                else:
                    print("dont say what you dont want")
                    return ""
