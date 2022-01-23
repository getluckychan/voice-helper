from pytg import Telegram

tg = Telegram(
    telegram="/usr/bin/snap/telegram-cli",
    pubkey_file="/home/ivan/PycharmProjects/pythonProject1/tg/tg-server.pub")
tg.start_cli()

