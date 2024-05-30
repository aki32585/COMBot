import math
import json
import discord
from discord import app_commands
from dispander import dispand

# intentsの設定
intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# コンフィグ読み込み
with open('config.json') as config_file:
    config_data = json.load(config_file)
    TOKEN = config_data.get('token', '')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await tree.sync()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    await dispand(message)

    # urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.content)

    # # "x.com"を含むURLが見つかった場合
    # for url in urls:
    #     if "https://x.com" in url:
    #         # URLを改変して新しいメッセージを生成
    #         modified_url = url.replace("x.com", "fxtwitter.com")
    #         # リプライで送る(メンションなし)
    #         await message.channel.send(f"{modified_url}", mention_author=False)
    # # "twitter.com"を含むURLが見つかった場合
    # for url in urls:
    #     if "https://twitter.com" in url:
    #         # URLを改変して新しいメッセージを生成
    #         modified_url = url.replace("twitter.com", "fxtwitter.com")

    #         # リプライで送る(メンションなし)
    #         await message.channel.send(f"{modified_url}", mention_author=False)
    if message.content.startswith("!hyouketsu"):
            h1 = message.content.split(" ")
            print(h1)
            try:
                h2 = int(h1[1])
            except:
                 await message.reply("エラー：入力データが無効です。数値を入力してください。",ephemeral=True)
            h2 = round(h2 / 170)
            print(h2)
            await message.reply(f"🍶🤖<氷結{str(h2)}本買えるのに...", mention_author=False)

@tree.command(name="hyouketsu",description="入力された金額で何本の氷結350ml缶が買えるか計算します")
async def test_command(interaction: discord.Interaction,price:int):
        price = math.floor(price / 170)
        text = (f"🍶🤖<氷結{str(price)}本買えるのに...")
        await interaction.response.send_message(text)
            
client.run(TOKEN)
