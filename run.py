import discord
from client import Client
from dotenv import load_dotenv
from os import getenv
import sys

def main():
    load_dotenv()
    TOKEN = getenv('TOKEN')
    GUILD = getenv('GUILD')

    if TOKEN is None:
        print('Please enter a TOKEN variable inside .env file.')
        sys.exit(1)

    if GUILD is None:
        print('Please enter a GUILD variable inside .env file.')
        sys.exit(1)

    try:
        GUILD = int(GUILD)
    except ValueError:
        print('GUILD must be a valid Discord server ID.')
        sys.exit(1)

    client = Client(GUILD)
    try:
        client.run(TOKEN)
    except discord.LoginFailure:
        print('Failed to log into Discord.')

if __name__ == '__main__':
    main()
