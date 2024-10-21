from telethon import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
from dotenv import  load_dotenv
import os

load_dotenv()

api_id = os.getenv('TELEGRAM_API_ID')
api_hash = os.getenv('TELEGRAM_API_HASH')
phone_number = os.getenv('TELEGRAM_PHONE_NUMBER')

client = TelegramClient('anon', api_id,api_hash)
    #await client.send_message('user','message')

async def scrape_messages(client, channel, limit):
    print(f"\n Scrapping messages from {channel} ... \n")

    async for message in client.iter_messages(channel, limit):
        if(message.text):
            print(message.text)
            print('-'*30)
        
        if isinstance(message.media, MessageMediaPhoto):
            photo_path = await message.download_media()
            print("Photo saved to:", photo_path)

async def main():
    channel_links = [
         'https://t.me/news_crypto', 
         'https://t.me/bitcoinnews', 
         'https://t.me/altcoinnews', 
         ]
    for channel_link in channel_links:
        await scrape_messages(client,channel_link,2)

with client:
    client.loop.run_until_complete(main())


