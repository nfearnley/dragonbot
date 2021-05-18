from discord.ext import commands

from dragonbot.lib.dragon import DragonCode


class CodeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dc(self, ctx, *, message: str):
        try:
            dragon = DragonCode.parse(message)
        except Exception as e:
            await ctx.send(f":warning: {e}")

        await ctx.send(f"DragonCode {dragon}")


def setup(bot):
    bot.add_cog(CodeCog(bot))
