import os
import sys
from dotenv import load_dotenv
from src.Client import Client
from src.OverwatchArcadeModes import OverwatchArcadeModes

load_dotenv()

if len(sys.argv) != 2:
    raise Exception('Expected exactly one argument: \'channel_id\', this is obtained by right clicking a channel in '
                    'Discord with developer mode enabled.')

# Initialize Discord Client
client = Client()
client.channel_id = int(sys.argv[1])
client.arcade_mode = OverwatchArcadeModes.TOTAL_MAYHEM

# Run Discord Client
client.run(os.environ.get('APP_TOKEN'))
