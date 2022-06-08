import discord
import os
import requests
import json
from time import time

client = discord.Client()

keywords = ["Fuck","fuck","Shit","shit","Asshole","asshole", "Skank", "skank", "Whore", "whore",
 "Piss", "piss", "Pussy","pussy",  "Cunt", "cunt", "Faggot","faggot", "Tits", "tits", "Titties","titties", "Nigga", "nigga",
 "Nigger", "nigger", "Goddamn", "goddamn", "Clit", "clit", "Dick", "dick",
 "Bitch", "bitch", "Chink","chink", "Cock","cock", "Damn", "damn","Dammit","dammit"]

@client.event
async def on_ready():
    print("We have logged in as {0.user}. I'm ready!".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$Wazzup"):
        await message.channel.send("Wazzup Brotha in Christ!")

    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(1):
                await message.delete()
                await message.channel.send("You are not allowed to use this word...REPENT!!.....")

@client.event
async def on_voice_state_update(member, before, after):

    if not before.channel and after.channel and member.id == 591388257992835093:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[591388257992835093] > 9000:
            graceperiods[591388257992835093] = time()
            await channel.send('Look out! Here comes the Amazing RPM...Man!')
            await channel.send(file=discord.File("Gifs/Spider-Man Theamazingrpm Gif.gif"))
        
    elif not before.channel and after.channel and member.id == 243879095711170572:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[243879095711170572] > 9000:
            graceperiods[243879095711170572] = time()
            await channel.send("Viktir is in VC! What else is new?")
            await channel.send(file=discord.File("Gifs/Viktir.gif"))

    elif not before.channel and after.channel and member.id == 598168727363780609:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[598168727363780609] > 9000:
            graceperiods[598168727363780609] = time()
            await channel.send("Everyone act busy! King Helgi approaches!")
            await channel.send(file=discord.File("Gifs/King Helgi.gif"))

    elif not before.channel and after.channel and member.id == 279776159120621568:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[279776159120621568] > 9000:
            graceperiods[279776159120621568] = time()
            await channel.send("Look out!! It's Friction!")
            await channel.send(file=discord.File("Gifs/Friction.gif"))

    elif not before.channel and after.channel and member.id == 702852168717303919:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[702852168717303919] > 9000:
            graceperiods[702852168717303919] = time()
            await channel.send("Is that YoungK in VC?!?")
            await channel.send(file=discord.File("Gifs/YoungK.gif"))

    elif not before.channel and after.channel and member.id == 629746673605804043:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[629746673605804043] > 9000:
            graceperiods[629746673605804043] = time()
            await channel.send(
            "Hey Look! It's Jillybillysillydillywillychilli! Just be grateful she doesn't give her last name!"
        )
            await channel.send(file=discord.File("Gifs/Jilly.gif"))

    elif not before.channel and after.channel and member.id == 180950627310895104:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[180950627310895104] > 9000:
            graceperiods[180950627310895104] = time()
            await channel.send("creativeSavagery Enters!")
            await channel.send(file=discord.File("Gifs/CreativeSavagery.gif"))

    elif not before.channel and after.channel and member.id == 669370838478225448:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[669370838478225448] > 9000:
            graceperiods[669370838478225448] = time()
            await channel.send("@Thegiggler is in VC! Everyone get ready for the trolling to happen!!")
            await channel.send(file=discord.File("Gifs/Thegiggler.gif"))

    elif not before.channel and after.channel and member.id == 684462242082717787:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[684462242082717787] > 9000:
            graceperiods[684462242082717787] = time()
            await channel.send("Taco is here!!")
            await channel.send(file=discord.File("Gifs/TacoKat.gif"))

    elif not before.channel and after.channel and member.id == 149151239597195264:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[149151239597195264] > 7200:
            graceperiods[149151239597195264] = time()
            await channel.send("Seal's here!")
            await channel.send(file=discord.File("Gifs/Seal.gif"))

    elif not before.channel and after.channel and member.id == 802677718515843072:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[802677718515843072] > 9000:
            graceperiods[802677718515843072] = time()
            await channel.send("Hippity hop! Bunny is here!")
            await channel.send(file=discord.File("Gifs/Bunny.gif"))

    elif not before.channel and after.channel and member.id == 309654076885303307:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[309654076885303307] > 9000:
            graceperiods[309654076885303307] = time()
        await channel.send("Grey Goat straggled in! Someone grab him!")
        await channel.send(file=discord.File("Gifs/GreyGoat.gif"))

    elif not before.channel and after.channel and member.id == 671382987459526668: 
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[671382987459526668] > 9000:
            graceperiods[671382987459526668] = time()
            await channel.send("Hey...it's Play-Doh...oh no, I mean Plato!")
            await channel.send(file=discord.File("Gifs/Plato.gif"))
    
    elif not before.channel and after.channel and member.id == 770390699131797565:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[770390699131797565] > 9000:
            graceperiods[770390699131797565] = time()
            await channel.send("Did I hear someone say a conspiracy is in the channel?...no, it's Mr. Conspiracle! Welcome back!!")
            await channel.send(file=discord.File("Gifs/Mr. Conspiracle.gif"))
    
    elif not before.channel and after.channel and member.id == 672142596209901580:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[672142596209901580] > 9000:
            graceperiods[672142596209901580] = time()
            await channel.send("Well hello! It's Sam!")
            await channel.send(file=discord.File("Gifs/Sam.gif"))
    
    elif not before.channel and after.channel and member.id == 929790100928340048:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[929790100928340048] > 9000:
            graceperiods[929790100928340048] = time()
            await channel.send("Everyone grab your Bible! NeilSpirits is in VC.")
            await channel.send(file=discord.File("Gifs/NeilSpirits.gif"))

    elif not before.channel and after.channel and member.id == 873204571298742323:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[873204571298742323] > 9000:
            graceperiods[873204571298742323] = time()
            await channel.send("Who let the Frog out of its cage? Oh, nevermind, it's Ribbit!")
            await channel.send(file=discord.File("Gifs/Ribbit.gif"))
    
    elif not before.channel and after.channel and member.id == 216674941238640640:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[216674941238640640] > 9000:
            graceperiods[216674941238640640] = time()
            await channel.send("Lo and Behold, Mr. Kit is here...Everyone gather around!")
            await channel.send(file=discord.File("Gifs/Mr. Kit.gif"))

    elif not before.channel and after.channel and member.id == 295015576038932480:
        channel = client.get_channel(982466476663509093)
        if time() - graceperiods[295015576038932480] > 9000:
            graceperiods[295015576038932480] = time()
            await channel.send("Hank Hill is back! Go ask him about his Propane and Propane accessories!!")
            await channel.send(file=discord.File("Gifs/Hank Hill.gif"))
    
graceperiods = {
    591388257992835093 : 0,
    243879095711170572 : 0,
    598168727363780609 : 0,
    279776159120621568 : 0,
    969608624307601438 : 0,
    629746673605804043 : 0,
    180950627310895104 : 0,
    669370838478225448 : 0,
    684462242082717787 : 0,
    149151239597195264 : 0,
    802677718515843072 : 0,
    309654076885303307 : 0,
    671382987459526668 : 0,
    770390699131797565 : 0,
    672142596209901580 : 0,
    929790100928340048 : 0,
    873204571298742323 : 0,
    216674941238640640 : 0,
    295015576038932480 : 0
}

@client.event
async def disconnect_member(member, before, after):
    role = client.get_role(983128803486367754)
    channel = client.get_channel(978095031560830976)
    member = channel.get_member(id)
    if role == False:
        if before.channel is None and after.channel is not None:
            await member.move_to(None)

client.run("INSERT_TOKEN_HERE")
