import discord
import asyncio
client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as:")
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print("Ready to use")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("Hello"):
        await client.send_message (message.channel, "Hi!")

client.run("your_token")
