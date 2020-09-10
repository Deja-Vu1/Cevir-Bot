import discord
from discord.ext import commands
from googletrans import Translator
import googletrans
from discord.ext import tasks
from bs4 import BeautifulSoup
import requests
from docx import Document
from docx.shared import Inches
# This bot doing anything :D, Made by love <3

PERFIX = ">"
bot = commands.Bot(command_prefix=PERFIX)
bot.remove_command('help')
chk = 0

@tasks.loop(minutes=5.0)
async def func1():
    await bot.change_presence(
        activity=discord.Game(
            name=">yardim & >help | 🌐 " + str(len(bot.guilds)) + " servers | Made by DejaVu#4515\n"))


@bot.command(aliases=['langs', 'languages', 'dil'])
async def diller(ctx):
    if str(ctx.message.channel.type) == "private":
        await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
    else:
        dsc = ""

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

@bot.command(aliases=['aramak', 'arat', 'search'])
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
                    await ctx.message.channel.send("{0}, Ops! I didn't find your search - Aramanı bulamadım".format(ctx.message.author.mention),delete_after=5.0)
                    await ctx.message.delete()
                                
        else:
            await ctx.message.delete()
            await ctx.message.channel.send("{0}, Please type language - Lütfen dil yazınız".format(ctx.message.author.mention),delete_after=5.0)

@bot.command(aliases=['clean','silsüpür'])
async def purge(ctx,limit=''):
    if ctx.message.author.guild_permissions.administrator:          # if you are administrator
        if limit != "":
            await ctx.message.channel.purge(limit=int(limit))
        else:
            await ctx.message.channel.purge()
    else:
        await ctx.message.channel.send("{0.author.mention}, şşş! kimse görmesin\nbu komudu kullanmamalısın".format(ctx.message),delete_after=5.0)
        await ctx.message.delete()

@bot.command()
async def sıfır(ctx,mess=''):
    global chk
    if str(ctx.message.channel.type) == "private":
        await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
    else:
        if str(ctx.message.author.id) == "596455467585110016":
            chk = 0
            await ctx.message.channel.send("{0.author.mention}, Done!".format(ctx.message),delete_after=5.0)
        else:
            await ctx.message.channel.send("{0.author.mention}, şşş! kimse görmesin\nbu komudu kullanmamalısın".format(ctx.message),delete_after=5.0)
            await ctx.message.delete()

@bot.command(aliases=['doküman','doc','word'])
async def docx(ctx,mess=''):
    if str(ctx.message.channel.type) == "private":
        await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
    else:
        if mess != '':
            global chk
            if chk == 0:
                chk = 1
                document = Document()
                mess = mess.split("|")
                for i in range(len(mess)):
                    if mess[i] != "":
                        if mess[i][0] == "h":
                            document.add_heading(mess[i][1:len(mess[i])], 0)
                        elif mess[i][0] == "t":
                            document.add_paragraph(mess[i][1:len(mess[i])])
                        elif mess[i][0] == "m":
                            document.add_paragraph(
mess[i][1:len(mess[i])], style='List Bullet'
)
                        elif mess[i][0] == "l":
                            document.add_paragraph(
mess[i][1:len(mess[i])], style='List Number'
)
                
                document.save('example.docx')
                await ctx.message.channel.send("Done! - Oldu! {0}".format(ctx.message.author.mention),file=discord.File('example.docx'))
                chk = 0
            else:
                await ctx.message.channel.send("Please Try Again - Lütfen tekrar dene {0}".format(ctx.message.author.mention))
        else:
            await ctx.message.channel.send("Please fill in the required fields - Lütfen gerekli alanları doldurun {0}".format(ctx.message.author.mention))
        
    
    

@bot.command(aliases=['trans','cevir','translater'])
async def translate(ctx,cevir='',dest=''):

    dest = dest.lower()

    if str(ctx.message.channel.type) == "private":
        await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
    else:

        cevir = cevir.replace("`","")
        
        if cevir != "":
            if dest != '':
                translator = Translator()
                print(dest)
                try:
                    dil = googletrans.LANGUAGES[translator.detect(cevir,dest=dest).lang]
                    dil2 = googletrans.LANGUAGES[dest]
                    cevirisi = translator.translate(cevir,dest=dest).text
                    await ctx.message.channel.send("{0.author.mention}, where did you find this language?\nTranslated language : {1}\nDestination Language: {3}\n```{2}```".format(ctx.message,dil,cevirisi,dil2))
                except:
                    await ctx.message.channel.send("{0.author.mention}, Ops!\nwrite enter valid language - geçerli bir dil girin".format(ctx.message),delete_after=5.0)
                    await ctx.message.delete()
            else:
                dest = 'en'
                translator = Translator()
                try:
                    dil = googletrans.LANGUAGES[translator.detect(cevir,dest=dest).lang]
                    dil2 = googletrans.LANGUAGES[dest]
                    cevirisi = translator.translate(cevir,dest=dest).text
                    await ctx.message.channel.send("{0.author.mention}, where did you find this language?\nTranslated language : {1}\nDestination Language: {3}\n```{2}```".format(ctx.message,dil,cevirisi,dil2))
                except:
                    await ctx.message.channel.send("{0.author.mention}, Ops!\nwrite enter valid language - geçerli bir dil girin".format(ctx.message),delete_after=5.0)
                    await ctx.message.delete()
        else:
            await ctx.message.channel.send("{0.author.mention}, Ops!\nwrite what you will translate - Neyi çevireceğini yaz...".format(ctx.message),delete_after=5.0)
            await ctx.message.delete()

@bot.command(aliases=['kelime', 'ogren'])
async def tdk(ctx,kelime=''):
    if str(ctx.message.channel.type) == "private":
        await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
    else:
        if kelime != "":
            try:
                from tdk import tdk
                word = tdk.new_word(kelime)
                description = word.meaning()[0]
                embed = discord.Embed(title="**TDK ANLAMLARI : {0}**".format(kelime.lower()), colour=discord.Colour(0x3b8ff0), description=description)   # Please check this link (https://discordjs.guide/popular-topics/embeds.html#embed-preview)
                embed.set_footer(text="Made by DejaVu#4515")
                embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                await ctx.message.channel.send(embed=embed)
            except:
                await ctx.message.channel.send("Yazdığın kelimenin doğru olduğundan emin ol\n**Bulacağımdan eminim** {0}".format(ctx.message.author.mention))

        else:
            await ctx.message.channel.send("{0}, Ops! I didn't find your search - Aramanı bulamadım".format(ctx.message.author.mention),delete_after=5.0)
            await ctx.message.delete()
                        
@bot.command(aliases=['gazete', 'resmi','haber'])
async def resmigazete(ctx):
    if str(ctx.message.channel.type) == "private":
        await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
    else:
        rsource = requests.get('https://www.resmigazete.gov.tr/')
        source = BeautifulSoup(rsource.content,"lxml")
        link = source.find("a",attrs={"id":"btnPdfGoruntule"}).get("href")
        yazi = source.find("div",attrs={"class":"html-subtitle"}).text
        aciklama2 = ""
        aciklama = source.find_all("a",attrs={"data-modal":"True"},limit=10)
        linka = source.find_all("a",attrs={"data-modal":"True"},limit=10)

        for i in range(len(aciklama)):
            aciklama2 += aciklama[i].text[0:len(aciklama[i].text)-15] + "[" + aciklama[i].text[len(aciklama[i].text)-15:len(aciklama[i].text)] + "](" + str(linka[i].get("href")) + ")\n\n"
        try:
            description = "[RESMİ GAZETE SON BASIM](" + str(link) + ")\n\n**" + yazi + "**\n\n" + aciklama2
            embed = discord.Embed(title="**RESMİ HABER**", colour=discord.Colour(0x3b8ff0), description=description)   # Please check this link (https://discordjs.guide/popular-topics/embeds.html#embed-preview)
            embed.set_footer(text="Made by DejaVu#4515")
            embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await ctx.message.channel.send(embed=embed,delete_after=60.0)
        except:
            rsource = requests.get('https://www.resmigazete.gov.tr/')
            source = BeautifulSoup(rsource.content,"lxml")
            link = source.find("a",attrs={"id":"btnPdfGoruntule"}).get("href")
            yazi = source.find("div",attrs={"class":"html-subtitle"}).text
            aciklama2 = ""
            aciklama = source.find_all("a",attrs={"data-modal":"True"},limit=5)
            linka = source.find_all("a",attrs={"data-modal":"True"},limit=5)
            for i in range(len(aciklama)):
                aciklama2 += aciklama[i].text[0:len(aciklama[i].text)-15] + "[" + aciklama[i].text[len(aciklama[i].text)-15:len(aciklama[i].text)] + "](" + str(linka[i].get("href")) + ")\n\n"

            description = "[RESMİ GAZETE SON BASIM](" + str(link) + ")\n\n**" + yazi + "**\n\n" + aciklama2
            embed = discord.Embed(title="**RESMİ HABER**", colour=discord.Colour(0x3b8ff0), description=description)   # Please check this link (https://discordjs.guide/popular-topics/embeds.html#embed-preview)
            embed.set_footer(text="Made by DejaVu#4515 | Maddeler çok uzundu kısalttık :D İyi okumalar")
            embed.set_author(name=ctx.message.author, icon_url=ctx.message.author.avatar_url)
            embed.set_thumbnail(url=ctx.message.author.avatar_url)
            await ctx.message.channel.send(embed=embed,delete_after=60.0)
           
@bot.command(aliases=['help', 'helps'])
async def yardim(ctx):
    if str(ctx.message.channel.type) == "private":
        await ctx.message.channel.send("{0} ,Sorry I can't help you - Üzgünüm sana yardım edemem".format(ctx.message.author.mention),delete_after=5.0)
    else:
        try:
            channel = await ctx.message.author.create_dm()
            await channel.send("""
{0}
:partying_face::partying_face::partying_face:
_**COMMANDS**_

**>cevir** _"A Word To Translate - Çevrilecek Olan Kelime" "Destination Language (default english) - Hedef Dil (Varsayılan ingilizce)"_

```Yazdığınız kelimeyi hedef dile göre çevirir - Translates your typed word according to the target language``` Aliases: 'trans', 'cevir', 'translater' , 'translate'
**>diller**
```Dm kutunuza dilleri gönderir - sends languages ​​to your dm box``` Aliases: 'languages', 'dil', 'diller', 'langs'
**>ara** _"dillerin kısaltmalarını arayın - Search for abbreviations of languages"_
```Bulunduğunuz yere dilin kısaltmasını gönderir - Sends the abbreviation of the language to your location``` Aliases: 'aramak', 'arat', 'ara', 'search'
**>tdk** _"Sözcüklerin anlamlarını tdk'den aratır - Search the meaning of words from tdk"_
```Sözcüklerin anlamlarını tdk'den aratır - Search the meaning of words from tdk``` Aliases: 'kelime', 'ogren'
**>haber** _"Resmi gaztenin güncel halini gösterir - Shows the current state of the official newspaper"_
```Resmi gaztenin güncel halini gösterir - Shows the current state of the official newspaper``` Aliases: 'gazete', 'resmi','haber'
**>docx**
_"tbaşına t eklediğiniz şeyler normal paragraf olarak eklenir|
mBaşına m koyduğun şeyler BİRER madde olarak eklenir|
l Başına l koyduğun şeyler BİRER sıralı madde olarak eklenir|
h Başına h koyduğunuz şeyler BİRER başlık olarak eklenir"_

EXAMPLE: >docx "hBU BİR BAŞLIK|tİÇİNDEKİLER|lYazılım nasıl yapılır?|lYazılımcı nasıl olunur?"
P.S : | <-- bu işaret "Alt Gr" + "-" ile yapılır  ,  Tırnak içine aldığınız formatta bir daha tırnak kullanmayınız (tek tırnak hariç)
```Sizin istediğin gibi bir Docx dosyası oluşturur - Creates a Docx file as you want it``` Aliases: 'doküman','doc','word'
:partying_face::partying_face::partying_face:
""".format(ctx.message.author.mention))
            await ctx.message.channel.send("{0} ,Sended dm to you for commands - Dm kutunuza komutlar gönderildi".format(ctx.message.author.mention),delete_after=5.0)
        except:
            await ctx.message.channel.send("{0} ,I can't send dm to you - Sana dm gönderemiyorum".format(ctx.message.author.mention),delete_after=15.0)


@bot.event
async def on_ready():
    await bot.change_presence(
    activity=discord.Game(
    name=">yardim & >help | 🌐 " + str(len(bot.guilds)) + " servers | Made by DejaVu#4515\n"))
    func1.start()

bot.run('TOKEN')
