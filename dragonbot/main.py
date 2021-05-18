import logging
from datetime import datetime

from discord.ext import commands

from dragonbot import conf

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("dragonbot")

initial_cogs = [
    "code"
]


def main():
    try:
        conf.load()
    except FileNotFoundError as e:
        logger.error(f"Configuration file not found: {e.filename}")
        return

    booting = True
    launchtime = datetime.now()

    bot = commands.Bot(command_prefix=conf.prefix)

    for cog in initial_cogs:
        bot.load_extension("dragonbot.cogs." + cog)

    async def on_first_ready():
        logger.info(f"Logged in as: {bot.user.name} ({bot.user.id})\n------")
        logger.info(f"Prefix: {conf.prefix}")
        launchfinishtime = datetime.now()
        elapsed = launchfinishtime - launchtime
        logger.debug(f"DragonBot launched in {round((elapsed.total_seconds() * 1000), 3)} milliseconds.\n")

    async def on_reconnect_ready():
        logger.error("DragonBot has been reconnected to Discord.")

    @bot.event
    async def on_ready():
        # Split on_ready into two events: one when we first boot, and one for reconnects.
        nonlocal booting
        if booting:
            await on_first_ready()
            booting = False
        else:
            await on_reconnect_ready()

    @bot.event
    async def on_message(message):
        await bot.process_commands(message)

    @bot.event
    async def on_message_edit(before, after):
        if before.content == after.content:
            return
        await bot.process_commands(after)

    @bot.event
    async def on_disconnect():
        logger.error("DragonBot has been disconnected from Discord!")

    if not conf.authtoken:
        logger.error("Authentication token not found!")
        return

    bot.run(conf.authtoken)


if __name__ == "__main__":
    main()
