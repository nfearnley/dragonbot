from discord.ext import commands


class CodeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dc(self, ctx, *, message: str):
        await ctx.send(f"DragonCode {message}")


def setup(bot):
    bot.add_cog(CodeCog(bot))
