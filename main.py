import os

import loguru
from phue import Bridge
from dotenv import load_dotenv
from discord.ext.commands import Bot

load_dotenv(override=True)

# Get parameters from .env
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
IP_PHUE = os.getenv("IP_PHUE")
INPUT_USERNAME = os.getenv("INPUT_USERNAME")
LIGHT_SOURCE = [int(i) for i in list(os.getenv("LIGHT_SOURCE"))]

_DEBUG =  os.getenv("DEBUG", False)
client = Bot(command_prefix="$")

bhue = Bridge(IP_PHUE, config_file_path=".python_hue")
bhue.connect()
bhue.get_api()

if _DEBUG:
    lights = bhue.lights
    loguru.logger.debug(lights)
    loguru.logger.debug(bhue.get_light().keys())

@client.event
async def on_voice_state_update(member, before, after):
    """ 
    Set philips hue light source to a 
    color when self_muted in dicord
    """
    _member = str(member).split("#")[0]
    if _DEBUG:
        loguru.logger.debug(f"{_member} - After{after}")

    if INPUT_USERNAME == _member:
        bhue.set_light(LIGHT_SOURCE,'on', True)
        if after.self_mute:
            # Red light, 100% brightness
            for ls in LIGHT_SOURCE:
                bhue[ls].hue = 65000
                bhue.set_light(ls, "bri", 100)
        else:
            # Green light, 100% brightness
            for ls in LIGHT_SOURCE:
                bhue[ls].hue = 20000
                bhue.set_light(ls, "bri", 100)

client.run(DISCORD_TOKEN)