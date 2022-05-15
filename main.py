import discord
import os
import requests
import json
from time import time

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}. I'm ready!".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$Wazzup"):
        await message.channel.send("Wazzup Brotha in Christ!")


@client.event
async def on_voice_state_update(member, before, after):

    if not before.channel and after.channel and member.id == 591388257992835093:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[591388257992835093] > 7200:
            graceperiods[591388257992835093] = time()
            await channel.send('Look out! Here comes the Amazing RPM...Man!')
            await channel.send(file=discord.File("Gifs/Spider-Man Theamazingrpm Gif.gif"))
        
    elif not before.channel and after.channel and member.id == 243879095711170572:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[243879095711170572] > 7200:
            graceperiods[243879095711170572] = time()
            await channel.send("Viktir is in VC! What else is new?")
            await channel.send(file=discord.File("Gifs/Viktir.gif"))

    elif not before.channel and after.channel and member.id == 598168727363780609:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[598168727363780609] > 7200:
            graceperiods[598168727363780609] = time()
            await channel.send("Everyone act busy! King Helgi approaches!")
            await channel.send(file=discord.File("Gifs/King Helgi.gif"))

    elif not before.channel and after.channel and member.id == 279776159120621568:
        channel = client.get_channel()
        if time() - graceperiods[279776159120621568] > 7200:
            graceperiods[279776159120621568] = time()
            await channel.send("Look out!! It's Friction!")
            await channel.send(file=discord.File("Gifs/Friction.gif"))

    elif not before.channel and after.channel and member.id == 969608624307601438:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[969608624307601438] > 7200:
            graceperiods[969608624307601438] = time()
            await channel.send("Is that YoungK in VC?!?")
            await channel.send(file=discord.File("Gifs/YoungK.gif"))

    elif not before.channel and after.channel and member.id == 629746673605804043:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[629746673605804043] > 7200:
            graceperiods[629746673605804043] = time()
            await channel.send(
            "Hey Look! It's Jillybillysillydillywillychilli! Just be grateful she doesn't give her last name!"
        )
            await channel.send(file=discord.File("Gifs/Jilly.gif"))

    elif not before.channel and after.channel and member.id == 180950627310895104:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[180950627310895104] > 7200:
            graceperiods[180950627310895104] = time()
            await channel.send("creativeSavagery Enters!")
            await channel.send(file=discord.File("Gifs/CreativeSavagery.gif"))

    elif not before.channel and after.channel and member.id == 669370838478225448:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[669370838478225448] > 7200:
            graceperiods[669370838478225448] = time()
            await channel.send("Oh no! Look who the circus just dragged back in...The Giggler!?!")
            await channel.send(file=discord.File("Gifs/TheGiggler.gif"))

    elif not before.channel and after.channel and member.id == 684462242082717787:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[684462242082717787] > 7200:
            graceperiods[684462242082717787] = time()
            await channel.send("Taco is here!!")
            await channel.send(file=discord.File("Gifs/TacoKat.gif"))

    elif not before.channel and after.channel and member.id == 149151239597195264:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[149151239597195264] > 7200:
            graceperiods[149151239597195264] = time()
            await channel.send("Seal's here!")
            await channel.send(file=discord.File("Gifs/Seal.gif"))

    elif not before.channel and after.channel and member.id == 802677718515843072:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[802677718515843072] > 7200:
            graceperiods[802677718515843072] = time()
            await channel.send("Hippity hop! Bunny is here!")
            await channel.send(file=discord.File("Gifs/Bunny.gif"))

    elif not before.channel and after.channel and member.id == 309654076885303307:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[309654076885303307] > 7200:
            graceperiods[309654076885303307] = time()
        await channel.send("Grey Goat straggled in! Someone grab him!")
        await channel.send(file=discord.File("Gifs/GreyGoat.gif"))

    elif not before.channel and after.channel and member.id == 671382987459526668: 
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[671382987459526668] > 7200:
            graceperiods[671382987459526668] = time()
            await channel.send("Hey...it's Play-Doh...oh no, I mean Plato!")
            await channel.send(file=discord.File("Gifs/Plato.gif"))
    
    elif not before.channel and after.channel and member.id == 770390699131797565:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[770390699131797565] > 7200:
            graceperiods[770390699131797565] = time()
            await channel.send("Did I hear someone say a conspiracy is in the channel?...no, it's Mr. Conspiracle! Welcome back!!")
            await channel.send(file=discord.File("Gifs/Mr. Conspiracle.gif"))
    
    elif not before.channel and after.channel and member.id == 672142596209901580:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[672142596209901580] > 7200:
            graceperiods[672142596209901580] = time()
            await channel.send("Well hello! It's Sam!")
            await channel.send(file=discord.File("Gifs/Sam.gif"))
    
    elif not before.channel and after.channel and member.id == 929790100928340048:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[929790100928340048] > 7200:
            graceperiods[929790100928340048] = time()
            await channel.send(file=discord.File("Everyone grab your Bible! NeilSpirits is in VC."))
            await channel.send(file=discord.File("Gifs/NeilSpirits.gif"))

    elif not before.channel and after.channel and member.id == 873204571298742323:
        channel = client.get_channel(834913896237236244)
        if time() - graceperiods[873204571298742323] > 7200:
            graceperiods[873204571298742323] = time()
            await channel.send ("Who let the Frog out of its cage? Oh, nevermind, it's Ribbit!")
            await channel.send(file=discord.File("Gifs/Ribbit.gif"))
            
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
    873204571298742323 : 0
}

client.run("OTcwMTMwMjA5Njg2ODE4ODg3.GPef58.IWDnJ4C2hn-lBekfN_k1WsocVyITXm5Kk0WMJg")
