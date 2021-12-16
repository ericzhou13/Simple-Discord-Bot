import time
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import glob
import csv
#TOKEN = Put token here

bot = commands.Bot(command_prefix="!")#makes the bot prefix
token = "Put Token Here"#
client = discord.Client()#creates and instance of the client that connects to discord


folder = glob.glob("File Location")
f = open("Discord\Photos.txt", "r")
f1 = open("Discord\count.txt", "a")
f1.close()


lines = f.read().split('\n')
for i in range(len(lines)):
	lines[i] = str(lines[i])
print(lines[1])

@client.event
async def on_message(message):
	id = client.get_guild("Server ID")
	#channels = ["General"]
	f1 = open("Discord\count.txt", "r")

	count = int(f1.read())
	
	#if str(message.channel) in channels:
	if message.content.find("!send") != -1:
		print(len(lines))
		print(count)
		while count < len(lines):
			await message.channel.send(file=discord.File(f"""File Location"""))
			await message.channel.send("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
			await message.channel.send("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
			count += 1
			f1 = open("Discord\count.txt", "w")
			f1.write(str(count))
			f1.close()
			time.sleep(1)
	
	f1.close()


client.run(token)




