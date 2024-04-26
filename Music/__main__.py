import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from Music import LOGGER, app, userbot
from Music.core.call import Lilly
from Music.misc import sudo
from Music.plugins import ALL_MODULES
from Music.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


loop = asyncio.get_event_loop_policy().get_event_loop()

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"Music.plugins{all_module}")
    LOGGER("Music.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Lilly.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("Music").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Lilly.decorators()
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("Music").info("Stopping Your Music Bot...")


if __name__ == "__main__":
    loop.run_until_complete(init())
