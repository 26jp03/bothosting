import discord
import openpyxl
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-------------------")
    print("ready")
    game = discord.Game("빵신봇을 작동 중...")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith('안녕하세요'):
        msg = '{0.author.mention} 어서오세요 #🔔규칙방🔔 봐주시고 #💬수다방💬 에서 소통하세요'.format(message)
        await message.channel.send(msg)
        
    if message.content.startswith("ㅎㅇ"):
        msg = '{0.author.mention} 어서오세요 #🔔규칙방🔔 봐주시고 #💬수다방💬 에서 소통하세요'.format(message)
        await message.channel.send(msg)
        
        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
