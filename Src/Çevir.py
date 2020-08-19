import discord
from discord.ext import commands
from googletrans import Translator
import googletrans

perfix = "?"
bot = commands.Bot(command_prefix=perfix)
bot.remove_command('help')

@bot.command()
async def çevir(ctx,çevir=''):
        
        if çevir != "":
                translator = Translator()
                dil = googletrans.LANGUAGES[translator.detect(çevir,dest='tr').lang]
                çevirisi = translator.translate(çevir,dest='tr').text
                await ctx.message.channel.send("{0.author.mention}, Bu dili nereden buldun?\nÇevirilen Dil : {1}\nÇevirdiği Dil: Türkçe\n```{2}```".format(ctx.message,dil,çevirisi))
        else:
                await ctx.message.channel.send("{0.author.mention}, Hani anlaşmıştık!\nLütfen çevireceğin şeyi yaz".format(ctx.message),delete_after=5.0)
                await ctx.message.delete()

@bot.command()
async def help(ctx):
        await ctx.message.channel.send("""
{0}
:partying_face::partying_face::partying_face:
**KOMUTLAR**

?çeviri "otomatik çevrilecek kelime"

:partying_face::partying_face::partying_face:
""".format(ctx.message.author.mention),delete_after=15.0)
        await ctx.message.delete()

@bot.event
async def on_ready():
        await bot.change_presence(activity=discord.Game(name="Made by DejaVu#4515"))

bot.run('Token')
