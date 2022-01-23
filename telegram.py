from telethon import TelegramClient, events, sync
import telethon

api_id = 16670165
api_hash = '2722d07b09eca2398c2e309548cab261'

client = TelegramClient('telegram_app', api_id, api_hash)
# client.session.set_dc(dc_id="149.154.167.40:443", server_address='149.154.167.40', port=80)

print(client.get_me())
client.ch

async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('yx3_3xy', 'Hello to myself!')


@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')

with client:
    client.start()
    client.run_until_disconnected()
