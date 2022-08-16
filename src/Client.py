import time

import discord
import requests
from discord import TextChannel
from discord.ext import tasks


class Client(discord.Client):
    channel_id: int
    channel: TextChannel
    arcade_mode: str

    check = '✅'
    cross = '❌'

    overwatch_today_uri: str = 'https://api.overwatcharcade.today/api/v1/overwatch/today'

    async def on_ready(self):
        print(f'Started bot, initializing channel with id: \'{self.channel_id}\'')

        self.channel = self.get_channel(self.channel_id)

        self.task.start()

    @tasks.loop(hours=1)
    async def task(self):
        total_mayhem_available = self.is_arcade_mode_available()

        await self.channel.edit(name=f'total-mayhem-{self.check if total_mayhem_available else self.cross}️')

        print(f'Synced {self.arcade_mode} at {str(time.time())}, available: \'{str(total_mayhem_available)}\'')

    def is_arcade_mode_available(self):
        request = requests.get(self.overwatch_today_uri)

        if request.status_code == 200:
            data = request.json()['data']

            return data['isToday'] and any(x['name'] == self.arcade_mode for x in data['modes'])
