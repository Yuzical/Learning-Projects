import discord
from discord.ext import commands
import random
import os


client = commands.Bot(command_prefix="~", intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")


@client.command(aliases=["8ball", "eightball", "magicball"])
async def m8(ctx, *, question):
    with open("M8B/Responses.txt", "r", encoding="utf-8") as f:
        random_responses = f.readlines()
        response = random.choice(random_responses)

    # Determine whether to send a message or a picture
    send_message = random.choice([True, False])

    if send_message:
        await ctx.send(response)
    else:
        # Choose a random picture from a folder
        picture_folder = "M8B/Pictures"  # Update this with your folder path
        picture_files = os.listdir(picture_folder)
        random_picture = random.choice(picture_files)

        # Construct the full file path
        picture_path = os.path.join(picture_folder, random_picture)

        # Send the picture
        with open(picture_path, "rb") as picture:
            await ctx.send(file=discord.File(picture))


client.run("MTE2MjYwNjkxOTgxNTUzNjcwMg.GTcgBN.U3FpxTMRX6T7vcG4YBiUsnUz7LaC6Pc8RQKIPU")
