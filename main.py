from telethon import TelegramClient, events
import requests

api_id = 123456  # 替换为您自己的 Telegram API ID
api_hash = 'your_api_hash'  # 替换为您自己的 Telegram API 哈什
webhook_url = 'your_webhook_url'  # 替换为您自己的企业微信机器人的 webhook URL

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=('channel_username',)))
async def handle_message(event):
    message = event.message.message
    
    # 过滤掉包含特定关键字的消息
    if 'keyword' not in message:
        return
    
    # 将消息转发到企业微信
    data = {'msgtype': 'text', 'text': {'content': message}}
    headers = {'Content-Type': 'application/json'}
    requests.post(webhook_url, json=data, headers=headers)

client.start()
client.run_until_disconnected()
