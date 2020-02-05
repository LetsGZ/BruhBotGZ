import discord

from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = '')
client.remove_command('help')

'''///---///'''

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='bruh-help'))
    print('Bot is ready :)')

'''///---///'''

@client.event
async def on_message(message):

    if message.author.bot == False:
        text = message.content.replace(" ", "")

        blacklist = ["bot"] # Bot does not react to messages that use a blacklist word with bruh
        
        words = message.content.split(" ")

        if len(words) == 1:
            if "bruh" == message.content:
                await message.channel.send(message.content)
        elif len(words) < 3:
            if "bruh" == words[0].lower() or "bruh" == words[1].lower():
                if words[0].lower() in blacklist or words[1].lower() in blacklist:
                    print("Word was in blacklist")
                else:
                    print("Sent a bruh")
                    await message.channel.send(message.content)
                    
        if message.content == "bruh-help":
            print('bruh-help has been used.')
            embed = discord.Embed(title="BruhBotGZ - Help", description="When you say Bruh the bot bruh's back, same with Bruh Moment. :)", color=0x444444)
            embed.set_author(name="BruhBotGZ", icon_url='https://bruhbot.letsgz.net/LetsGZ/LetsGZ.png')
            embed.add_field(name="bruh-help", value="this is what you're using right now!", inline=False)
            embed.add_field(name="bruh-info", value="Info about this bot.", inline=False)
            embed.set_thumbnail(url='https://bruhbot.letsgz.net/LetsGZ/LetsGZ.png')
            embed.set_footer(text="Thank you for using this bot! <3")
            await message.channel.send(embed=embed)

        if message.content == "bruh-info":
            print('bruh-info has been used.')
            embed = discord.Embed(title="BruhBotGZ", description="This bot was made by LetsGZ (https://letsgz.net)", color=0x444444, url="https://bruhbot.letsgz.net")
            embed.set_author(name="BruhBotGZ", icon_url='https://bruhbot.letsgz.net/LetsGZ/LetsGZ.png')
            embed.add_field(name="Big thanks to Dounut", value="http://dounut.tech", inline=False)
            embed.add_field(name="BruhBotGZ invite link", value="https://bruhbot.letsgz.net", inline=False)
            embed.add_field(name="BruhBotGZ source code", value="https://github.com/LetsGZ/BruhBotGZ", inline=False)
            embed.set_thumbnail(url='https://bruhbot.letsgz.net/LetsGZ/LetsGZ.png')
            embed.set_footer(text="Thank you for using this bot! <3")
            await message.channel.send(embed=embed)

'''///---///'''

client.run("BOT TOKEN")
