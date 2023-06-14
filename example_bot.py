# This example requires the 'message_content' intent.

import discord, json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    admins = [
        "Lucas 5.0#0407"
    ]
    content = message.content
    if "hello" in str.lower(content):
        await message.channel.send('Hello!')
        await message.channel.send(f"my name is {client.user}")
    if "goodbye" in str.lower(content):
        await message.channel.send('Goodbye, ' + str(message.author))
        if str(message.author) in admins:
            await message.channel.send("I cannot kick you")
        else:
            await message.author.kick()
    if "!" in str.lower(content):
        await message.reply('NO SWEARING!')
        await message.delete(delay=None)

with open("./bot-key.json") as jsonFile:
    file = json.load(jsonFile)
    for item in file:
        key = file["key"]

client.run(key)
