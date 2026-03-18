import discord
from discord.ext        import commands
from colorama           import Fore
import time
import datetime
import os
from dotenv             import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

def discord_init(prefix: str):
    intents = discord.Intents.default()
    intents.message_content = True
    intents.moderation = True
    intents.guilds = True

    client = commands.Bot(command_prefix=prefix, intents=intents)
    return client

client = discord_init("(IP2P) ")

def message(mss: str, fore: str, name_export, id_export):
    day = datetime.date.today().day
    month = datetime.date.today().month

    clock = time.strftime("%H:%M:%S")
    timezone = "Timezone: {}".format(time.timezone)
    
    try:
        fore = getattr(Fore, fore.upper())
    except AttributeError:
        fore = Fore.WHITE

    readymss = print(
        "BOT: {}{}".format(Fore.YELLOW, name_export), Fore.RESET,
        "\nID: {}{}".format(Fore.YELLOW, id_export), Fore.RESET+"\n"+
        fore, clock, "{}/{}".format(day, month), timezone, Fore.RESET, mss
        )
    
    return readymss
