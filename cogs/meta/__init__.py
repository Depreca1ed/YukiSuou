from __future__ import annotations

from typing import TYPE_CHECKING

from .avatar import Avatar
from .botinfo import BotInformation
from .roleinfo import RoleInfo
from .serverinfo import ServerInfo
from .userinfo import Userinfo

if TYPE_CHECKING:
    from bot import Lagrange


class Meta(Avatar, BotInformation, RoleInfo, Userinfo, ServerInfo, name='Meta'): ...


async def setup(bot: Lagrange) -> None:
    await bot.add_cog(Meta(bot))
