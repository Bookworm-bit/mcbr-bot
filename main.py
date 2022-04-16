import discord
import os
from discord.ext import commands
from time import sleep
intents = discord.Intents().all()
intents.members = True

bot = commands.Bot(command_prefix="]", intents=intents)
ping = []
people = ""
pingmsg = "This week these people asked to play MC: "
points = {}

@bot.event
async def on_connect():
  print("connected")

@bot.event
async def on_member_join(member):
  points[str(member.id)] = 0

@bot.event
async def on_message(message):
  await bot.process_commands(message)
  guild = bot.get_guild(message.guild.id)
  for member in guild.members:
    points[member.id] = 0
      #points[f'{person}'] = 0
  points[message.author.id] = 0
  points.get(message.author.id)
  if message.author == bot.user:
    return
  if 'bedrock' in message.content:
    points[message.author.id] += 1 
  if 'play' in message.content:
    points[message.author.id] += 2
  if 'war' in message.content:
    points[message.author.id] += 1.5
  if 'anyone' in message.content:
    points[message.author.id] += 1
  if 'hive' in message.content:
    points[message.author.id] += 2
  if 'who' in message.content:
    points[message.author.id] += 0.5
  if 'dm' in message.content:
    points[message.author.id] += 0.5
  if 'interest' in message.content:
    points[message.author.id] += 1
  if 'survival' in message.content:
    points[message.author.id] += 2
  if points[message.author.id] >= 3.1:
    ping.append(f'<@{message.author.id}>')
    await message.channel.send("For friends I'd suggest looking in <#864405889490485248>, for realms/servers to play on I suggest you look in <#864423583236227102> Alternatively, we have an smp you could join with about a weeks wait time, for more info on that read <#853336509419749376> We are also partnered with a awesome discord server called Minecraft: Supernova that is host to multiple amazing minigames and realms, for more info on that you can check <#917508508579160064>")

@bot.command(name="buddy")
async def ping_week(ctx: commands.Context):
  people = ', '.join(ping)
  await ctx.send(pingmsg + people)
  await ctx.send(points)

bot.run(os.getenv("token"))