from discord.ext import commands
import discord
import os
import random
import requests
from threading import Thread
from flask import Flask
import pymongo
import psutil


bot = commands.Bot(command_prefix='cf ')

app = Flask(__name__)

coinflip = ['heads', 'tails']
mongodb_key = os.getenv('mongokey')

@app.route('/')
def hello_world():
  return 'Chill Bot'

token = os.getenv('token')
authorid = os.getenv('author')
noperms_message = 'Lacking perms'
counting_channel_id = 816740701865639972
embed_color = 0x484848

bot.remove_command('help')

bad_words = list(os.getenv('badwords'))

client = pymongo.MongoClient("mongodb://dbUser:"+mongodb_key+"@cluster0-shard-00-00.xoe4b.mongodb.net:27017,cluster0-shard-00-01.xoe4b.mongodb.net:27017,cluster0-shard-00-02.xoe4b.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-rj95f3-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.money.coins

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Chill Bot | Prefix: cf"))
  print(f'{bot.user.name} has connected to Discord!')

# Economy Commands

def addcoins(id, amount):
  db.update_one(
    {
    'id': id
    },
    {
      '$inc': {
        'coins': amount
      }
    },
    upsert=True
  )

@bot.command()
async def shootout(ctx, user: discord.User, amount):
  amount = int(amount)
  addcoins(user.id, amount*-1)
  addcoins(ctx.author.id, amount*-1)
  embed=discord.Embed(color=embed_color)
  embed.add_field(name="Shootout", value=f'You and <@{user.id}> both lost {amount}', inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def gamble(ctx, amount):
  embed=discord.Embed(color=embed_color)
  balance = db.find_one({'id': ctx.author.id})
  coins = balance['coins']
  amount = int(amount)
  if coins >= int(amount):
    choice = random.choice(coinflip)
    if choice == 'tails':
      addcoins(ctx.author.id, amount*-1)
      embed.add_field(name="Gamble", value=f'Lost {amount} ChillCoins', inline=False)
    elif choice == 'heads':
      addcoins(ctx.author.id, amount)
      embed.add_field(name="Gamble", value=f'Won {amount} ChillCoins', inline=False)
  else:
    embed.add_field(name="Gamble", value=f'Not enough ChillCoins, need {amount} have {coins}', inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def donate(ctx, user: discord.User, amount):
  embed=discord.Embed(color=embed_color)
  balance = db.find_one({'id': ctx.author.id})
  coins = balance['coins']
  amount = int(amount)
  if coins >= int(amount):
      embed.add_field(name="Donate", value=f'Donated {amount} ChillCoins to <@{user.id}>', inline=False)
      addcoins(ctx.author.id, amount*-1)
      addcoins(user.id, amount)
  else:
    embed.add_field(name="Donate", value=f'Not enough ChillCoins, need {amount} have {coins}', inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def duel(ctx, user: discord.User, amount):
  embed=discord.Embed(color=embed_color)
  balance = db.find_one({'id': ctx.author.id})
  amount = int(amount)
  if balance['coins'] >= amount:
    choice = random.choice(coinflip)
    if choice == 'heads':
      addcoins(ctx.author.id, amount)
      addcoins(user.id, amount*-1)
      embed.add_field(name="Duel", value=f'<@{ctx.author.id}> stole {amount} from <@{user.id}>', inline=False)
    elif choice == 'tails':
      addcoins(ctx.author.id, amount*-1)
      addcoins(user.id, amount*1)
      embed.add_field(name="Duel", value=f'<@{user.id} stole {amount} from <@{ctx.author.id}>', inline=False)
  else:
    embed.add_field(name="Duel", value=f'Not enough ChillCoins, have {balance["coins"]} need {amount}', inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def bal(ctx, user: discord.User=None):
  embed=discord.Embed(color=embed_color)
  if user is None:
    balance = db.find_one({"id": ctx.author.id})
    embed.add_field(name="Balance", value=f'You have {balance["coins"]} ChillCoins', inline=False)
  else:
    balance = db.find_one({"id": user.id})
    embed.add_field(name="Balance", value=f'<@{user.id}> has {balance["coins"]} ChillCoins', inline=False)
  await ctx.send(embed=embed)

# Moderation Commands

@bot.command()
async def mute(ctx, user: discord.User):
  embed=discord.Embed(color=embed_color)
  if ctx.author.guild_permissions.administrator:
    await user.add_roles(discord.utils.get(ctx.message.guild.roles, name='Muted'))
    embed.add_field(name="Mute", value=f'<@{user.id}>', inline=False)
  else:
    embed.add_field(name="Mute", value=noperms_message, inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def unmute(ctx, user: discord.User):
  embed=discord.Embed(color=embed_color)
  if ctx.author.guild_permissions.administrator:
    await user.remove_roles(discord.utils.get(ctx.message.guild.roles, name='Muted'))
    embed.add_field(name="Unmute", value=f'<@{user.id}>', inline=False)
  else:
    embed.add_field(name="Unmute", value=noperms_message, inline=False)
    await ctx.send(noperms_message)
  await ctx.send(embed=embed)

@bot.command()
async def kick(ctx, user: discord.User):
  embed=discord.Embed(color=embed_color)
  if ctx.author.guild_permissions.administrator:
    await ctx.guild.kick(user, reason='Kicked')
    embed.add_field(name="Kick", value=f'<@{user.id}>', inline=False)
  else:
    embed.add_field(name="Kick", value=noperms_message, inline=False)
    await ctx.send(noperms_message)
  await ctx.send(embed=embed)

@bot.command()
async def pardon(ctx, user: discord.User):
  embed=discord.Embed(color=embed_color)
  if ctx.author.guild_permissions.administrator:
    await ctx.guild.unban(user)
    embed.add_field(name="Pardon", value=f'<@{user.id}>', inline=False)
  else:
    embed.add_field(name="Pardon", value=noperms_message, inline=False)
    await ctx.send(noperms_message)
  await ctx.send(embed=embed)

@bot.command()
async def ban(ctx, user: discord.User):
  embed=discord.Embed(color=embed_color)
  if ctx.author.guild_permissions.administrator:
    await ctx.guild.ban(user, reason='Banned')
    embed.add_field(name="Ban", value=f'<@{user.id}>', inline=False)
  else:
    embed.add_field(name="Ban", value=noperms_message, inline=False)
    await ctx.send(noperms_message)
  await ctx.send(embed=embed)

@bot.command()
async def clean(ctx, limit: int):
  embed=discord.Embed(color=embed_color)
  if ctx.author.guild_permissions.administrator:
    await ctx.channel.purge(limit=limit)
    embed.add_field(name="Purge", value=str(limit)+' messages', inline=False)
  else:
    embed.add_field(name="Purge", value=noperms_message, inline=False)
    await ctx.send(noperms_message)
  await ctx.send(embed=embed)

@bot.command()
async def user(ctx, user: discord.User):
  embed = discord.Embed(title=f"{user.name}'s Stats", color=embed_color)
  embed.set_thumbnail(url=str(user.avatar_url))
  embed.add_field(name="Name", value=user.name, inline=False)
  embed.add_field(name="ID", value=user.id, inline=False)
  embed.add_field(name="Tag", value=user.discriminator, inline=False)
  embed.add_field(name="Account Creation", value=user.created_at.strftime('%Y-%m-%d at %H:%M:%S'), inline=False)
  embed.add_field(name="Bot", value=user.bot, inline=False)
  await ctx.send(embed=embed)

# Fun Commands 
@bot.command()
async def meme(ctx):
  response = requests.get("https://meme-api.herokuapp.com/gimme/memes")
  response = response.json()
  embed = discord.Embed(color=embed_color)
  embed.add_field(name=response['title'], value='r/memes', inline=True)
  embed.set_image(url=response['url'])
  await ctx.send(embed=embed)

@bot.command()
async def joke(ctx):
  j = requests.get("http://official-joke-api.appspot.com/jokes/random")
  j = j.json()
  embed = discord.Embed(title="Joke", description="Dad Jokes", color=embed_color)
  embed.add_field(name="Joke", value=j['setup'], inline=False)
  embed.add_field(name="Punchline", value=j['punchline'], inline=False)
  embed.add_field(name="Joke Number", value=j['id'], inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
  embed=discord.Embed(color=embed_color)
  embed.add_field(name="Ping", value=str(round(bot.latency*1000, 1))+' ms', inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def status(ctx):
  pid = os.getpid()
  py = psutil.Process(pid)
  embed = discord.Embed(color=embed_color, title="Resource Usage")
  embed.add_field(name="RAM", value=str(round(py.memory_info()[0]/1000000, 1))+'MB')
  embed.add_field(name="CPU", value=str(psutil.cpu_percent())+'%')
  await ctx.send(embed=embed)

# Help Commands

@bot.command()
async def adminhelp(ctx):
  embed = discord.Embed(title="Admin Help Page", color=embed_color)
  embed.add_field(name="cf clean [int:messages]", value="Purge certain number of messages", inline=False)
  embed.add_field(name="cf mute/unmute [id/ping:user]", value="Mutes or unmutes a user", inline=False)
  embed.add_field(name="cf ban/pardon [id/ping:user]", value="Ban or unban a user", inline=False)
  embed.add_field(name="cf kick [id/ping:user]", value="Kick a user", inline=False)
  await ctx.send(embed=embed)

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Help Page", color=embed_color)
  embed.add_field(name="cf user [id/ping:user]", value="Data for a user", inline=False)
  embed.add_field(name="cf ping", value="Get bot latency", inline=False)
  embed.add_field(name="cf joke", value="Get a random joke", inline=False)
  embed.add_field(name="cf meme", value="Get a reddit meme", inline=False)
  await ctx.send(embed=embed)

# Counting System

@bot.event
async def on_message(message):
  addcoins(message.author.id, 10)
  if message.channel.id == counting_channel_id:
    lastMessage = await message.channel.history(limit=2).flatten()
    lm = lastMessage[1]
    try:
      if int(message.content) == int(lm.content) + 1:
        await message.add_reaction('\N{THUMBS UP SIGN}')
      else:
        await message.delete()
    except:
      await message.delete()
  await bot.process_commands(message)

def start_bot():
  app.run(host="0.0.0.0",port="8000")
Thread(None, start_bot).start()
bot.run(token)
