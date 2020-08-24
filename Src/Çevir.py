import discord
from discord.ext import commands
from googletrans import Translator
import googletrans

perfix = ">"
bot = commands.Bot(command_prefix=perfix)
bot.remove_command('help')

@bot.command()
async def diller(ctx):
        if str(ctx.message.channel.type) == "private":
                await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
        else:
                dsc = ""

                print(ctx.message.author.status)
                print(ctx.message.author.dm_channel)
                channel = await ctx.message.author.create_dm()
        
                for i in googletrans.LANGUAGES:
                        dsc += str(i) + " : " + googletrans.LANGUAGES[i] + "\n"

                embed = discord.Embed(title="**DİLLER - LANGUAGES**", colour=discord.Colour(0x3b8ff0), description=dsc)   # Please check this link (https://discordjs.guide/popular-topics/embeds.html#embed-preview)
                embed.set_footer(text="Made by DejaVu#4515")
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
        
                await channel.send(embed=embed)
                await ctx.message.channel.send("{0} ,Sended dm to you for languages - Dm kutunuza diller gönderildi".format(ctx.message.author.mention),delete_after=5.0)
                await ctx.message.delete()

@bot.command()
async def ara(ctx,dil=''):
        if str(ctx.message.channel.type) == "private":
                await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
        else:
                if dil != '':
                        dil = dil.lower()
                        chk = 0
                        for i,j in googletrans.LANGUAGES.items():
                                if dil in j:
                                        chk = 1
                                        await ctx.message.channel.send("{0}, Language : {1}".format(ctx.message.author.mention,i),delete_after=15.0)
                                        await ctx.message.delete()
                        if chk == 0:
                               await ctx.message.channel.send("{0}, Ops! I didn't find your search".format(ctx.message.author.mention),delete_after=5.0)
                               await ctx.message.delete()
                                
                else:
                        await ctx.message.delete()
                        await ctx.message.channel.send("{0}, Please type language - Lütfen dil yazınız".format(ctx.message.author.mention),delete_after=5.0)

@bot.command()
async def cevir(ctx,çevir='',dest=''):

        if str(ctx.message.channel.type) == "private":
                await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
        else:

                çevir = çevir.replace("`","")
                çevir = çevir.replace("_","")
                çevir = çevir.replace("*","")
                çevir = çevir.replace("@","")
        
                if çevir != "":
                        if dest != '':
                                translator = Translator()
                                dil = googletrans.LANGUAGES[translator.detect(çevir,dest=dest).lang]
                                dil2 = googletrans.LANGUAGES[dest]
                                çevirisi = translator.translate(çevir,dest=dest).text
                                await ctx.message.channel.send("{0.author.mention}, where did you find this language?\nTranslated language : {1}\nDestination Language: {3}\n```{2}```".format(ctx.message,dil,çevirisi,dil2))
                        else:
                                dest = 'en'
                                translator = Translator()
                                dil = googletrans.LANGUAGES[translator.detect(çevir,dest=dest).lang]
                                dil2 = googletrans.LANGUAGES[dest]
                                çevirisi = translator.translate(çevir,dest=dest).text
                                await ctx.message.channel.send("{0.author.mention}, where did you find this language?\nTranslated language : {1}\nDestination Language: {3}\n```{2}```".format(ctx.message,dil,çevirisi,dil2))
                else:
                        await ctx.message.channel.send("{0.author.mention}, Ops!\nwrite what you will translate".format(ctx.message),delete_after=5.0)
                        await ctx.message.delete()

@bot.command()
async def yardim(ctx):
        if str(ctx.message.channel.type) == "private":
                await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
        else:
                await ctx.message.channel.send("""
{0}
:partying_face::partying_face::partying_face:
**COMMAND**

>cevir "A Word To Translate" "Destination Language (default english)" 
>cevir "Çevrilecek Olan Kelime" "Hedef Dil (Varsayılan ingilizce)"
```Yazdığınız kelimeyi hedef dile göre çevirir - Translates your typed word according to the target language```

>diller
```Dm kutunuza dilleri gönderir - sends languages ​​to your dm box```

>ara "dillerin kısaltmalarını arayın - Search for abbreviations of languages"
```Bulunduğunuz yere dilin kısaltmasını gönderir - Sends the abbreviation of the language to your location```

:partying_face::partying_face::partying_face:
""".format(ctx.message.author.mention),delete_after=15.0)
                await ctx.message.delete()

@bot.event
async def on_ready():
        await bot.change_presence(activity=discord.Game(name=">yardim Made by DejaVu#4515\n"))

bot.run('Token')
