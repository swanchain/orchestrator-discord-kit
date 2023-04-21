import csv
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('discord_token')
GUILD = os.getenv('discord_guild_id')

intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # Get guild
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    try:
        if guild is None:
            print(
                f'-- {client.user} is not connected to any guilds.'
            )
            return
        print(f'-- Logged on as {client.user}! \n'
              f'-- {client.user} is connected to the following guild: \n'
              f'-- {guild.name} (id: {guild.id})'
              )
    except Exception as e:
        print("-- Error: Failed to get guild")
        print(e)
        return
    # Create csv
    if os.path.exists('userInfo.csv'):
        print("-- userInfo.csv already exists, deleting it...")
        os.remove('userInfo.csv')
    try:
        with open('userInfo.csv', 'w', encoding='utf-8', newline='') as f:
            # Create csv writer
            writer = csv.writer(f)
            writer.writerow(
                ['name', 'discriminator', 'id', 'bot', 'created_at', 'status',
                 'user_full_name'])
            # get all guilds in client
            for guild in client.guilds:
                # get all members in guild
                for member in guild.members:
                    # get creation date
                    create = str(member.created_at.strftime("%d/%m/%Y %H:%M:%S"))
                    # write to csv
                    writer.writerow(
                        [str(member.name), str(member.discriminator), int(member.id), str(member.bot),
                         create, str(member.status), str(member.name + '#' + member.discriminator)])
    except Exception as e:
        print("-- Error: Failed to create userInfo.csv")
        print(e)
        return
    print("-- Finished, your file is ready in the same directory as this script.")

    try:
        # Close client
        await client.close()
    except Exception as e:
        # delete csv
        os.remove('userInfo.csv')
        print("-- Error: Failed to close client")
        print(e)
    return


client.run(TOKEN)
