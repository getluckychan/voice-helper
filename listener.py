from enum import Enum
from abc import ABC, abstractmethod
from os import system


class Command(ABC):
    def __init__(self, text):
        try:
            self.text = text.value
        except IndexError:
            self.text = "ne priletelo, a priletit po ebaly za takoe"
            pass

    @abstractmethod
    def check(self):
        pass


class OpenCommand(Command):
    class SysCommand(Enum):
        chrome = "google-chrome"
        telegram = "telegram-desktop"
        spotify = "spotify"

    def check(self):
        for cmd in self.text.split(" "):
            checking = ["open"
                        ]
            if cmd in checking:
                for command in self.SysCommand:
                    if command.name in self.text:
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

    def check(self):
        for cmd in self.text.split(" "):
            checking = ["volume",
                        "sound"
                        ]
            if cmd in checking:
                for command in self.SysCommand:
                    if command.name in self.text:
                        print("working: " + command.name)
                        system(command.value)


class SystemCommand(Command):
    def __init__(self):
        super().__init__(self.text)
        self.command_need_to_confirm = []

    class SysCommand(Enum):
        shutdown = "poweroff"
        reboot = "reboot"

    def check(self):
        com = self.text.split()
        com = ''.join(com)
        for command in self.SysCommand:
            if command.name in com:
                self.command_need_to_confirm.append(command.value)
                pass

    def check_bool(self):
        try:
            checking = {
                "yes": f'{self.command_need_to_confirm[0]}',
                "no": "dont say what you dont want"
            }
            print("are u sure")
            try:
                system(checking.get(self.text))
                print("don`t say what you want")
            except TypeError:
                pass
        except IndexError:
            pass
