from telethon import TelegramClient, events
import requests
import os

# 获取所有环境变量
env_vars = os.environ

# 打印环境变量的值
for key, value in env_vars.items():
    print(f'{key}: {value}')

# Get the environment variables from GitHub Actions
telegram_api_id = os.environ.get("TELEGRAM_API_ID")
telegram_api_hash = os.getenv("TELEGRAM_API_HASH")
webhook_url = os.getenv("WEBHOOK_URL")
channel_username = os.getenv("CHANNEL_USERNAME")
print("telegram_api_id:",telegram_api_id)
print("telegram_api_hash:",telegram_api_hash)
print("webhook_url:",webhook_url)
print("channel_username:",channel_username)
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
