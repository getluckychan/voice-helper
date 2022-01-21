from pytg import Telegram

tg = Telegram(
    telegram="/path/to/tg/bin/telegram-cli",
    pubkey_file="/home/ivan/PycharmProjects/pythonProject1/tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender
