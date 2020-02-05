import discord
import time

from discord.ext import commands
from discord.ext.commands import Bot

client = discord.Client()
a = 1

'''///---///'''    

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='bruh'))
    print('Bot is ready :)')
    
'''///---///'''    
    
@client.event
async def on_message(message):

    if message.author.bot == False:
        text = message.content.replace(" ", "")
        
        if text.lower().strip() == ("bruh"):
            await message.channel.send(message.content)
            print('bruh has been used.')
            
        if text.lower().strip() == ("bruhmoment"):
            await message.channel.send(message.content)
            print('bruhmoment has been used.')
            
        if text.lower().strip() == ("bruh-info"):
            await message.channel.send("Made by LetsGZ (https://letsgz.net) and Dounut (http://dounut.tech)")
            print('bruh-info has been used.')

'''///---///'''            

client.run("YOUR TOKEN")