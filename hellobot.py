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
        
    if message.content.startswith("ㅂ/사진목록"):
        one = "빵신사진"
        two = "바보"
        three = "이불"
        await message.channel.send(str(one)+', '+str(three)+'과 '+str(two))
    
    if message.content.startswith("ㅂ/사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))        
        
access_token = os.environ['BOT_TOKEN']
client.run(access_token)
