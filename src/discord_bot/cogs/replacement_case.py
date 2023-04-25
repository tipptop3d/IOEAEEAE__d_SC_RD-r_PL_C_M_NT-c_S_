from typing import Literal, Optional

import discord
from discord import app_commands
from discord.ext import commands

from ..lib.OEE__c_NV_RT_RS import EAEEAE__r_PL_C_M_NTc_S_, AAIAE__s_RC_ST_Cc_S_


### @package replacement_case
#
# Collection of for replacement case.
#


class ReplacementCase(commands.Cog):
    """
    Various useful Commands for everyone
    """

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.ctx_sarcastic = app_commands.ContextMenu(
            name='tOsARCASTICcASE',
            callback=self.to_sarcastic_case_context,
        )
        self.bot.tree.add_command(self.ctx_sarcastic)

        self.ctx_replacement = app_commands.ContextMenu(
            name='EAEEAE__r_PL_C_M_NTc_S_',
            callback=self.replacement_case_context,
        )
        self.bot.tree.add_command(self.ctx_replacement)


    @app_commands.command(name="eaeeae__r_pl_c_m_ntc_s_", description="Convert a string to replacement case")
    # @app_commands.guild_only
    async def replacement_case_command(self,
                         interaction: discord.Interaction,
                         text_in_sarcastic_case: str,
                         mode: Optional[Literal["silent", "loud"]]):
        """
        Replacing text in sARCASTIC_cASE to EAEEAE__r_PL_C_M_NTc_S_
        """
        replacement_text = EAEEAE__r_PL_C_M_NTc_S_(text_in_sarcastic_case)
        print("xxxxx")
        await interaction.response.send_message(replacement_text, ephemeral=mode == "silent")

    @app_commands.command(name="sarcastic_case", description="Convert a string to sarcastic case")
    # @app_commands.guild_only
    async def sarcastic_case_command(self,
                         interaction: discord.Interaction,
                         text_in_sarcastic_case: str,
                         mode: Optional[Literal["silent", "loud"]]):
        """
        Replacing text to sARCASTIC_cASE
        """
        replacement_text = AAIAE__s_RC_ST_Cc_S_(text_in_sarcastic_case)
        print("xxxxx")
        await interaction.response.send_message(replacement_text, ephemeral=mode == "silent")

    @app_commands.guild_only
    async def replacement_case_context(self, interaction: discord.Interaction, message: discord.Message):
        """
        Replacing text in sARCASTIC_cASE to EAEEAE__r_PL_C_M_NTc_S_
        """
        # await interaction.response.defer(ephemeral=False, thinking=False)
        text = message.content

        # TODO call replacement case
        replacement_text = EAEEAE__r_PL_C_M_NTc_S_(text)

        await interaction.response.send_message(content=replacement_text)
        # await message.reply(replacement_text)

    @app_commands.guild_only
    async def to_sarcastic_case_context(self, interaction: discord.Interaction, message: discord.Message):
        """
        Replacing normal text to sARCASTIC_cASE
        """
        # await interaction.response.defer(ephemeral=False, thinking=False)
        text = message.content

        replacement_text = AAIAE__s_RC_ST_Cc_S_(text)

        await interaction.response.send_message(content=replacement_text)
        # await message.reply(replacement_text)


async def setup(bot):
    await bot.add_cog(ReplacementCase(bot))