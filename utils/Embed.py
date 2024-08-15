from collections.abc import Iterable
from typing import (
    Any,
)

import discord
from discord.ext import commands

from bot import YukiSuou


class ElyEmbed(discord.Embed):
    """Main purpose is to get the usual setup of Embed for a command or an error embed"""

    def __init__(
        self,
        colour: discord.Colour | int = YukiSuou.colour,
        fields: Iterable[tuple[str, str]] = (),
        field_inline: bool = False,
        **kwargs: Any,
    ) -> None:
        super().__init__(colour=colour, **kwargs)
        for n, v in fields:
            self.add_field(name=n, value=v, inline=field_inline)

    @classmethod
    def default(
        cls,
        ctx: commands.Context[Any],
        colour: discord.Colour | int | None = None,
        **kwargs: Any,
    ) -> discord.Embed:
        instance = cls(**kwargs)
        instance.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.display_avatar.url or None,
        )
        if colour:
            instance.colour = colour
            return instance
        if ctx.author.id in ctx.bot.owner_ids:
            instance.colour = 0xFFFFFF
            return instance
        instance.colour = instance.colour
        return instance
