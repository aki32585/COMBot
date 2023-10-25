import discord
from dispander import dispand
import re
import json

# intentsの設定
intents=discord.Intents.all()
client = discord.Client(intents=intents)

#コンフィグ読み込み
with open('config.json') as config_file:
    config_data = json.load(config_file)
    TOKEN = config_data.get('token', '')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    await dispand(message)

    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)
    
    # "x.com"を含むURLが見つかった場合
    for url in urls:
        if "https://x.com" in url:
            # URLを改変して新しいメッセージを生成
            modified_url = url.replace("x.com", "fxtwitter.com")
            
            # ここに作動させたい処理を追加
            await message.reply(f"{modified_url}")
    for url in urls:
        if "https://twitter.com" in url:
            # URLを改変して新しいメッセージを生成
            modified_url = url.replace("twitter.com", "fxtwitter.com")
            
            # ここに作動させたい処理を追加
            await message.reply(f"{modified_url}", mention_author=False)

client.run(TOKEN)