# Overwatch Arcade Availability Discord Bot

Updates a Discord channel of your choosing with the availability of your favorite Overwatch Arcade mode! 
Currently only designed to work for Total Mayhem.

Many thanks to [overwatch.today](https://overwatcharcade.today/) for providing the required data.

# Usage
1. Obtain a Discord bot token from [here](https://discord.com/developers/applications).
2. With [developer mode](https://discord.com/developers/docs/game-sdk/store#application-test-mode) enabled in Discord, right-click a channel you would like to bind the bot to. Provide this channel id as the first positional argument for the script.
3. `pip3 install -r requirements.txt`
4. `python3 main.py <discord channel id>`
5. *Optionally*, run with [Docker](https://www.docker.com/): `docker build . -t tmbot && docker run tmbot <discord channel id>` 