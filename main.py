import os

from discord.member import Member


import discord
from discord import utils
from discord.ext import commands
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M")
TOKEN = "ВСТАВЬТЕ_ВАШ_ТОКЕН"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='prefix', intents=intents)


@bot.event
async def on_member_join(member):
  #now = datetime.now()
  emb = discord.Embed(
      title=f'@{member.name}, добро пожаловать на **{member.guild.name}**',
      color=0xff0000)
  emb.add_field(
      name="Есть на этом сервере правила?",
      value=
      'Конечно, есть! Перейди в канал "Правила" или нажми <#1149409873239482419>',
      inline=False)
  emb.add_field(
      name="Команды бота",
      value=
      'Чтобы узнать подробнее команды пропиши /help в канале `скоро добавлю`',
      inline=False)
  if member.discriminator == 0:
    emb.set_author(name=f'{member.name}')
  else:
    emb.set_author(name=f'{member.name}#{member.discriminator}')
  emb.set_footer(text=f'Ваш ID: {member.id} • {current_time}')
  channel = bot.get_channel(1119329001727606784)
  await channel.reply(mention_author=True, embed=emb)


@bot.event
async def on_member_remove(member):
  #now = datetime.now()
  emb = discord.Embed(
      title=
      f'Пока, @{member.name}, надеюсь, ты вернешься в гильдию **{member.guild.name}** :cry:',
      color=0xff0000)
  emb.set_footer(text=f'Ваш ID: {member.id} • {current_time}')
  channel = bot.get_channel(1119329001727606784)
  await channel.reply(mention_author=True, embed=emb)

bot.run(TOKEN)
