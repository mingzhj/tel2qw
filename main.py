from telethon import TelegramClient, events
import requests
import os

# Get the environment variables from GitHub Actions
telegram_api_id = os.environ["TELEGRAM_API_ID"]
telegram_api_hash = os.environ["TELEGRAM_API_HASH"]
webhook_url = os.environ["WEBHOOK_URL"]
channel_username = os.environ["CHANNEL_USERNAME"]

client = TelegramClient('my_tekegram', telegram_api_id, telegram_api_hash)

@client.on(events.NewMessage(chats=(channel_username,)))
async def handle_message(event):
    message = event.message.message
    
    # 过滤掉包含特定关键字的消息
    if '高速' not in message:
        return
    
    # 将消息转发到企业微信
    data = {'msgtype': 'text', 'text': {'content': message}}
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, json=data, headers=headers)

client.start()
client.run_until_disconnected()
