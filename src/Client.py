import discord
import requests
from discord import TextChannel
from discord.ext import tasks

from src.OverwatchArcadeModes import OverwatchArcadeModes


class Client(discord.Client):
    channel_id: int
    mayhem_channel: TextChannel

    check = '✅'
    cross = '❌'

    async def on_ready(self):
        print(f'Started bot, initializing channel with id: \'{self.channel_id}\'')

        self.mayhem_channel = self.get_channel(self.channel_id)

        self.task.start()

    @tasks.loop(hours=1)
    async def task(self):
        total_mayhem_available = self.is_arcade_mode_available(OverwatchArcadeModes.TOTAL_MAYHEM)

        await self.mayhem_channel.edit(name=f'total-mayhem-{self.check if total_mayhem_available else self.cross}️')

        await self.mayhem_channel.send('test')

    def is_arcade_mode_available(self, mode: str):
        request = requests.get('https://api.overwatcharcade.today/api/v1/overwatch/today')

        if request.status_code == 200:
            data = request.json()['data']

            return data['isToday'] and any(x['name'] == mode for x in data['modes'])
