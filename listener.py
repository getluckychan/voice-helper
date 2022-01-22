from enum import Enum
from abc import ABC, abstractmethod
from os import system
from time import sleep

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
        text = text.lower()
        for command in self.SysCommand:
            if command.name in text:
                command_need_to_confirm.append(command.value)
                pass
